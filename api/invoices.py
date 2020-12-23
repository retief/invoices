def parse_field(field):
    label = field["label"]
    text = field["text"]
    confidence = field["confidence"][label]
    return (label, text, confidence)


def parse_fields(fields):
    out = {}
    for label, text, confidence in map(parse_field, fields):
        if label in out:
            old_confidence = out[label][1]
        else:
            old_confidence = -1
        if confidence > old_confidence:
            out[label] = (text, confidence)
    return {label: text for (label, (text, confidence)) in out.items()}


def parse_invoice(api_response):
    model = api_response["results"]["document"]["results"]["Invoice Fields q2026 model"]
    return parse_fields(model["final"])
