# Simple compliance rule checker
# You will later integrate real Basel rules

def check_compliance(document_text: str) -> list:
    keywords = ["Liquidity Coverage Ratio", "Net Stable Funding Ratio", "Intraday Liquidity"]
    gaps = []
    for kw in keywords:
        if kw.lower() not in document_text.lower():
            gaps.append(f"Missing: {kw}")
    return gaps
