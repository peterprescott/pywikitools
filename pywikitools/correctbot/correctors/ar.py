from typing import List
from .base import CorrectorBase
from .universal import QuotationMarkCorrector, UniversalCorrector, RTLCorrector


class ArabicCorrector(CorrectorBase, UniversalCorrector, RTLCorrector, QuotationMarkCorrector):
    """
    Correct Arabic typos:
    * Arabic quotations start with start with “ and end with ”
      (at least that's what we're doing for now, in some contexts also «quote» is used)
    * Common corrections from UniversalCorrector and RTLCorrector
    """
    def correct_quotes(self, text: str) -> str:
        """Ensure correct Arabic quotes (example: “اقتباس”)"""
        return self._correct_quotes('“', '”', text)

    def _capitalization_exceptions(self) -> List[str]:
        return []

    def _missing_spaces_exceptions(self) -> List[str]:
        return []
