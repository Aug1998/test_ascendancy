import re

def get_normalized_list(values):
    # Keep only non-empty strings and normalize surrounding whitespace.
    raw_names = [name for name in values if isinstance(name, str)]
    normalized_unique = {name.strip() for name in raw_names if name.strip()}

    # Sort by length (shortest first) so root brands become canonical first.
    sorted_names = sorted(normalized_unique, key=lambda n: (len(n), n.casefold()))

    canonical_roots = []
    normalized_mapping = {}

    # Match names based on shared starting words (case-insensitive).
    for normalized_name in sorted_names:
        canonical_match = None

        for canonical in canonical_roots:
            pattern = rf"^{re.escape(canonical)}(\b|$)"
            if re.match(pattern, normalized_name, flags=re.IGNORECASE):
                canonical_match = canonical
                break

        if canonical_match is None:
            canonical_match = normalized_name
            canonical_roots.append(canonical_match)

        normalized_mapping[normalized_name] = canonical_match

    # Return mapping for original names while reusing the normalized canonical lookup.
    return {
        original_name: normalized_mapping[original_name.strip()]
        for original_name in raw_names
        if original_name.strip()
    }
