#!/usr/bin/env python3
"""
Proofreading Skill Implementation
Review manuscript chapters for grammar, style, pacing, and formatting issues.
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


class Proofreader:
    """Chapter proofreading and analysis engine."""

    def __init__(self, chapter_title: str = None):
        self.chapter_title = chapter_title
        self.findings = {
            'critical': [],
            'style': [],
            'grammar': [],
            'pacing': [],
            'formatting': []
        }
        self.recommendations = []

    def read_chapter(self, text: str) -> str:
        """Store chapter text for analysis."""
        self.text = text.strip()
        return self.text

    def analyze(self) -> Dict[str, List[str]]:
        """Run all proofreading checks."""
        self.check_em_dashes()
        self.check_contractions()
        self.check_dialogue_formatting()
        self.check_pacing()
        self.check_spelling_patterns()
        self.analyze_voice_consistency()
        return self.compile_report()

    def check_em_dashes(self):
        """Flag em dash usage (author prefers to avoid)."""
        # Look for long dashes (em dashes)
        em_dash_pattern = r'—'
        matches = re.findall(em_dash_pattern, self.text)
        if matches:
            self.findings['grammar'].append(
                f"Found {len(matches)} em dash(s) — consider using commas or parentheses instead"
            )
            # Find context
            positions = [m.start() for m in re.finditer(em_dash_pattern, self.text)]
            for pos in positions[:5]:  # Show first 5
                context = self.text[max(0, pos-30):min(len(self.text), pos+30)]
                context = context.replace('\n', ' ').strip()
                if context:
                    self.findings['grammar'].append(f"  Context: '{context}'")

    def check_contractions(self):
        """Count and note contraction usage."""
        contraction_pattern = r"\b\w+'t|\b\w+''re|\b\w+''s|\b\w+''ve|\b\w+''ll|\b\w+''d\b"
        matches = re.findall(contraction_pattern, self.text)
        if matches:
            self.findings['style'].append(
                f"Found {len(matches)} contraction(s) — acceptable for dialogue, review for narrative"
            )

    def check_dialogue_formatting(self):
        """Check dialogue quotation and tag consistency."""
        # Count dialogue openings
        dialogue_opens = self.text.count('"') + self.text.count("'")
        dialogue_closes = self.text.count('"') + self.text.count("'")
        
        if dialogue_opens != dialogue_closes:
            self.findings['formatting'].append(
                f"Uneven dialogue quotes: {dialogue_opens} opens, {dialogue_closes} closes"
            )
        else:
            self.findings['style'].append(
                f"Found {dialogue_opens // 2} dialogue exchange(s) — check tag variety"
            )

        # Check for "said" overuse
        said_count = self.text.lower().count(' said ')
        if said_count > 5:
            self.recommendations.append(
                f"Dialogue uses 'said' {said_count} times — consider varying dialogue tags"
            )

    def check_pacing(self):
        """Identify potential pacing issues."""
        # Very long paragraphs (>300 chars)
        paragraphs = re.split(r'\n\n+', self.text)
        long_paragraphs = [p for p in paragraphs if len(p) > 300 and len(p) < 5000]
        
        if long_paragraphs:
            self.findings['pacing'].append(
                f"Found {len(long_paragraphs)} paragraph(s) over 300 characters — consider breaking for readability"
            )

        # Very short paragraphs (<2 sentences, standalone dialogue)
        short_paragraphs = [p for p in paragraphs if len(p.strip()) < 50 and p.strip()]
        if len(short_paragraphs) > 10:
            self.recommendations.append(
                f"Found {len(short_paragraphs)} very short paragraphs — may indicate rapid pacing or formatting issues"
            )

        # Check for scene break clarity
        scene_break_patterns = [
            r'\n\*\*\*\s*\n',
            r'\n~\s*~\s*~\n',
            r'\n—{3,}\n',
            r'\n\n{4,}'  # Multiple blank lines
        ]
        has_clear_breaks = any(re.search(pb, self.text) for pb in scene_break_patterns)
        if not has_clear_breaks and len(paragraphs) > 20:
            self.recommendations.append(
                "No clear scene breaks detected — consider adding *-* or --- for clarity"
            )

    def check_spelling_patterns(self):
        """Check for common spelling/grammar issues."""
        # Double letters that might be typos
        typo_pattern = r'\b(\w)\1{2,}\b'
        double_letters = re.findall(typo_pattern, self.text)
        if double_letters:
            self.findings['grammar'].append(
                f"Possible spelling errors: {' '.join(double_letters[:5])}"
            )

        # Inconsistent capitalization (proper nouns)
        # This is a simplified check
        pass

    def analyze_voice_consistency(self):
        """Check for voice and perspective consistency."""
        # Detect narrative tense
        past_tense_markers = r'\b\w+ed\b'
        past_matches = re.findall(past_tense_markers, self.text)
        
        present_tense_markers = r'\b\w+s\b'
        present_matches = re.findall(present_tense_markers, self.text)
        
        if len(past_matches) > len(present_matches) * 2:
            self.findings['style'].append(
                "Predominantly past tense narrative — consistent with most fiction"
            )
        elif len(present_matches) > len(past_matches) * 2:
            self.findings['style'].append(
                "Predominantly present tense narrative — ensure consistency throughout"
            )
        else:
            self.recommendations.append(
                "Mixed tense detected — verify intentional usage or consider standardizing"
            )

        # Detect perspective (first/third person)
        first_person = self.text.lower().count(' i ') + self.text.lower().count(' my ')
        third_person_he = self.text.lower().count(' he ') + self.text.lower().count(' him ')
        third_person_she = self.text.lower().count(' she ') + self.text.lower().count(' her ')
        
        if first_person > 20:
            self.findings['style'].append(
                "First-person narrative detected — maintain consistent 'I' perspective"
            )
        elif (third_person_he + third_person_she) > first_person * 2:
            self.findings['style'].append(
                "Third-person narrative detected — ensure consistent character POV"
            )

    def compile_report(self) -> Dict[str, List[str]]:
        """Compile all findings into structured report."""
        report = {
            'chapter': self.chapter_title or 'Untitled',
            'critical_issues': self.findings['grammar'][:5],  # Top 5 grammar issues
            'style_notes': self.findings['style'],
            'pacing_flags': self.findings['pacing'],
            'formatting_issues': self.findings['formatting'],
            'recommendations': self.recommendations
        }
        return report

    def generate_report_text(self, report: Dict[str, List[str]]) -> str:
        """Format report as readable text."""
        lines = [
            f"## Chapter: {report['chapter']} - Proofreading Report",
            "",
            f"### Critical Issues ({len(report['critical_issues'])} found)",
        ]
        
        for issue in report['critical_issues']:
            lines.append(f"  - {issue}")
        
        if report['style_notes']:
            lines.append(f"\n### Style Consistency ({len(report['style_notes'])} notes)")
            for note in report['style_notes']:
                lines.append(f"  • {note}")
        
        if report['pacing_flags']:
            lines.append(f"\n### Pacing & Flow ({len(report['pacing_flags'])} flags)")
            for flag in report['pacing_flags']:
                lines.append(f"  • {flag}")
        
        if report['formatting_issues']:
            lines.append(f"\n### Formatting ({len(report['formatting_issues'])} issues)")
            for issue in report['formatting_issues']:
                lines.append(f"  - {issue}")
        
        if report['recommendations']:
            lines.append(f"\n### Recommendations")
            for i, rec in enumerate(report['recommendations'], 1):
                lines.append(f"{i}. {rec}")
        
        lines.append(f"\n### Overall Assessment")
        
        total_issues = (
            len(report['critical_issues']) + 
            len(report['pacing_flags']) + 
            len(report['formatting_issues'])
        )
        
        if total_issues == 0:
            lines.append("Chapter appears clean — ready for final review.")
        elif total_issues <= 5:
            lines.append(f"Found {total_issues} issue(s) to address. Generally well-written.")
        else:
            lines.append(f"Found {total_issues} issue(s). Review recommendations before finalizing.")
        
        return '\n'.join(lines)


def main():
    """Run proofreading on provided text."""
    if len(sys.argv) < 2:
        print("Usage: python proofreading.py <chapter_text> [chapter_title]")
        sys.exit(1)

    chapter_text = sys.argv[1]
    chapter_title = sys.argv[2] if len(sys.argv) > 2 else None

    proofreader = Proofreader(chapter_title)
    proofreader.read_chapter(chapter_text)
    report = proofreader.analyze()
    formatted_report = proofreader.generate_report_text(report)
    
    print(formatted_report)


if __name__ == "__main__":
    main()
