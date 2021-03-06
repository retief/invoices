expected = {
    "Vendor Name": "Horse Hollow Press, Inc.",
    "Vendor City": "Goshen,",
    "Vendor State": "NY",
    "Vendor Zip": "10924",
    "Invoice #": "7251",
    "Invoice Date": "03/28/19",
}

original = {
    "submission_id": 9628,
    "etl_output": "indico-file:///storage/submission/933/9628/9628_etl_output.json",
    "errors": [],
    "results": {
        "document": {
            "results": {
                "Invoice Fields q2026 model": {
                    "pre_review": [
                        {
                            "start": 0,
                            "end": 24,
                            "label": "Vendor Name",
                            "text": "Horse Hollow Press, Inc.",
                            "confidence": {
                                "Vendor Street": 6.481331365648657e-05,
                                "Amount Due": 0.0011646089842543006,
                                "Invoice #": 6.472079257946461e-05,
                                "Invoice Date": 8.93189717317e-05,
                                "Vendor Zip": 0.0004907228285446763,
                                "Vendor City": 0.0012069031363353133,
                                "Due Date": 0.00015866683679632843,
                                "<PAD>": 0.02093402110040188,
                                "Vendor Name": 0.9748049378395081,
                                "Vendor State": 0.001021229662001133,
                            },
                        },
                        {
                            "start": 37,
                            "end": 44,
                            "label": "Vendor City",
                            "text": "Goshen,",
                            "confidence": {
                                "Vendor Street": 0.0011899317614734173,
                                "Amount Due": 0.0004137640353292227,
                                "Invoice #": 0.0001882733340607956,
                                "Invoice Date": 0.0003024839097633958,
                                "Vendor Zip": 0.0004531782178673893,
                                "Vendor City": 0.9254889488220215,
                                "Due Date": 2.8724023650283925e-05,
                                "<PAD>": 0.06762830913066864,
                                "Vendor Name": 0.0011006606509909034,
                                "Vendor State": 0.0032057464122772217,
                            },
                        },
                        {
                            "start": 45,
                            "end": 47,
                            "label": "Vendor State",
                            "text": "NY",
                            "confidence": {
                                "Vendor Street": 2.9875031032133847e-05,
                                "Amount Due": 0.00012008286284981295,
                                "Invoice #": 5.563406375586055e-05,
                                "Invoice Date": 8.745858940528706e-05,
                                "Vendor Zip": 0.00010129594738828018,
                                "Vendor City": 0.0001089719298761338,
                                "Due Date": 1.7356953321723267e-05,
                                "<PAD>": 0.0011443671537563205,
                                "Vendor Name": 0.00011105594603577629,
                                "Vendor State": 0.9982238411903381,
                            },
                        },
                        {
                            "start": 48,
                            "end": 53,
                            "label": "Vendor Zip",
                            "text": "10924",
                            "confidence": {
                                "Vendor Street": 9.093922017200384e-06,
                                "Amount Due": 1.836611954786349e-05,
                                "Invoice #": 0.0001155631834990345,
                                "Invoice Date": 2.229679375886917e-05,
                                "Vendor Zip": 0.9996457099914551,
                                "Vendor City": 8.524831173417624e-06,
                                "Due Date": 1.5336554497480392e-06,
                                "<PAD>": 0.0001617724192328751,
                                "Vendor Name": 4.45699697593227e-06,
                                "Vendor State": 1.261040597455576e-05,
                            },
                        },
                        {
                            "start": 105,
                            "end": 110,
                            "label": "Vendor Name",
                            "text": "ollow",
                            "confidence": {
                                "Vendor Street": 8.901915862224996e-05,
                                "Amount Due": 0.006064058747142553,
                                "Invoice #": 0.001211630180478096,
                                "Invoice Date": 0.0007451208075508475,
                                "Vendor Zip": 0.0010624941205605865,
                                "Vendor City": 0.007432334590703249,
                                "Due Date": 0.0005995807587169111,
                                "<PAD>": 0.4327414631843567,
                                "Vendor Name": 0.5493618845939636,
                                "Vendor State": 0.0006923704058863223,
                            },
                        },
                        {
                            "start": 332,
                            "end": 340,
                            "label": "Invoice Date",
                            "text": "03/28/19",
                            "confidence": {
                                "Vendor Street": 1.375246228008109e-07,
                                "Amount Due": 2.4829228095768485e-07,
                                "Invoice #": 2.999136268044822e-05,
                                "Invoice Date": 0.9999316334724426,
                                "Vendor Zip": 7.4051390583917964e-06,
                                "Vendor City": 7.661210474907421e-07,
                                "Due Date": 1.1973185110036866e-06,
                                "<PAD>": 2.5024646674864925e-05,
                                "Vendor Name": 2.9016950975346845e-07,
                                "Vendor State": 3.244154186177184e-06,
                            },
                        },
                        {
                            "start": 342,
                            "end": 346,
                            "label": "Invoice #",
                            "text": "7251",
                            "confidence": {
                                "Vendor Street": 5.199684892431833e-05,
                                "Amount Due": 0.0009916656417772174,
                                "Invoice #": 0.9954041838645935,
                                "Invoice Date": 0.0002794804167933762,
                                "Vendor Zip": 0.0013657950330525637,
                                "Vendor City": 1.4747303794138134e-05,
                                "Due Date": 1.6768290151958354e-05,
                                "<PAD>": 0.0017224911134690046,
                                "Vendor Name": 3.103340350207873e-05,
                                "Vendor State": 0.00012185724335722625,
                            },
                        },
                        {
                            "start": 456,
                            "end": 464,
                            "label": "Invoice Date",
                            "text": "03/28/19",
                            "confidence": {
                                "Vendor Street": 1.6936540703227365e-07,
                                "Amount Due": 3.640730028564576e-07,
                                "Invoice #": 2.7652289645629935e-05,
                                "Invoice Date": 0.9993146061897278,
                                "Vendor Zip": 4.309777978050988e-06,
                                "Vendor City": 1.8512110955271055e-06,
                                "Due Date": 8.932221135182772e-06,
                                "<PAD>": 0.0006339889951050282,
                                "Vendor Name": 9.724277560962946e-07,
                                "Vendor State": 7.157467280194396e-06,
                            },
                        },
                    ],
                    "final": [
                        {
                            "start": 0,
                            "end": 24,
                            "label": "Vendor Name",
                            "text": "Horse Hollow Press, Inc.",
                            "confidence": {
                                "Vendor Street": 6.481331365648657e-05,
                                "Amount Due": 0.0011646089842543006,
                                "Invoice #": 6.472079257946461e-05,
                                "Invoice Date": 8.93189717317e-05,
                                "Vendor Zip": 0.0004907228285446763,
                                "Vendor City": 0.0012069031363353133,
                                "Due Date": 0.00015866683679632843,
                                "<PAD>": 0.02093402110040188,
                                "Vendor Name": 0.9748049378395081,
                                "Vendor State": 0.001021229662001133,
                            },
                        },
                        {
                            "start": 37,
                            "end": 44,
                            "label": "Vendor City",
                            "text": "Goshen,",
                            "confidence": {
                                "Vendor Street": 0.0011899317614734173,
                                "Amount Due": 0.0004137640353292227,
                                "Invoice #": 0.0001882733340607956,
                                "Invoice Date": 0.0003024839097633958,
                                "Vendor Zip": 0.0004531782178673893,
                                "Vendor City": 0.9254889488220215,
                                "Due Date": 2.8724023650283925e-05,
                                "<PAD>": 0.06762830913066864,
                                "Vendor Name": 0.0011006606509909034,
                                "Vendor State": 0.0032057464122772217,
                            },
                        },
                        {
                            "start": 45,
                            "end": 47,
                            "label": "Vendor State",
                            "text": "NY",
                            "confidence": {
                                "Vendor Street": 2.9875031032133847e-05,
                                "Amount Due": 0.00012008286284981295,
                                "Invoice #": 5.563406375586055e-05,
                                "Invoice Date": 8.745858940528706e-05,
                                "Vendor Zip": 0.00010129594738828018,
                                "Vendor City": 0.0001089719298761338,
                                "Due Date": 1.7356953321723267e-05,
                                "<PAD>": 0.0011443671537563205,
                                "Vendor Name": 0.00011105594603577629,
                                "Vendor State": 0.9982238411903381,
                            },
                        },
                        {
                            "start": 48,
                            "end": 53,
                            "label": "Vendor Zip",
                            "text": "10924",
                            "confidence": {
                                "Vendor Street": 9.093922017200384e-06,
                                "Amount Due": 1.836611954786349e-05,
                                "Invoice #": 0.0001155631834990345,
                                "Invoice Date": 2.229679375886917e-05,
                                "Vendor Zip": 0.9996457099914551,
                                "Vendor City": 8.524831173417624e-06,
                                "Due Date": 1.5336554497480392e-06,
                                "<PAD>": 0.0001617724192328751,
                                "Vendor Name": 4.45699697593227e-06,
                                "Vendor State": 1.261040597455576e-05,
                            },
                        },
                        {
                            "start": 105,
                            "end": 110,
                            "label": "Vendor Name",
                            "text": "ollow",
                            "confidence": {
                                "Vendor Street": 8.901915862224996e-05,
                                "Amount Due": 0.006064058747142553,
                                "Invoice #": 0.001211630180478096,
                                "Invoice Date": 0.0007451208075508475,
                                "Vendor Zip": 0.0010624941205605865,
                                "Vendor City": 0.007432334590703249,
                                "Due Date": 0.0005995807587169111,
                                "<PAD>": 0.4327414631843567,
                                "Vendor Name": 0.5493618845939636,
                                "Vendor State": 0.0006923704058863223,
                            },
                        },
                        {
                            "start": 332,
                            "end": 340,
                            "label": "Invoice Date",
                            "text": "03/28/19",
                            "confidence": {
                                "Vendor Street": 1.375246228008109e-07,
                                "Amount Due": 2.4829228095768485e-07,
                                "Invoice #": 2.999136268044822e-05,
                                "Invoice Date": 0.9999316334724426,
                                "Vendor Zip": 7.4051390583917964e-06,
                                "Vendor City": 7.661210474907421e-07,
                                "Due Date": 1.1973185110036866e-06,
                                "<PAD>": 2.5024646674864925e-05,
                                "Vendor Name": 2.9016950975346845e-07,
                                "Vendor State": 3.244154186177184e-06,
                            },
                        },
                        {
                            "start": 342,
                            "end": 346,
                            "label": "Invoice #",
                            "text": "7251",
                            "confidence": {
                                "Vendor Street": 5.199684892431833e-05,
                                "Amount Due": 0.0009916656417772174,
                                "Invoice #": 0.9954041838645935,
                                "Invoice Date": 0.0002794804167933762,
                                "Vendor Zip": 0.0013657950330525637,
                                "Vendor City": 1.4747303794138134e-05,
                                "Due Date": 1.6768290151958354e-05,
                                "<PAD>": 0.0017224911134690046,
                                "Vendor Name": 3.103340350207873e-05,
                                "Vendor State": 0.00012185724335722625,
                            },
                        },
                        {
                            "start": 456,
                            "end": 464,
                            "label": "Invoice Date",
                            "text": "03/28/19",
                            "confidence": {
                                "Vendor Street": 1.6936540703227365e-07,
                                "Amount Due": 3.640730028564576e-07,
                                "Invoice #": 2.7652289645629935e-05,
                                "Invoice Date": 0.9993146061897278,
                                "Vendor Zip": 4.309777978050988e-06,
                                "Vendor City": 1.8512110955271055e-06,
                                "Due Date": 8.932221135182772e-06,
                                "<PAD>": 0.0006339889951050282,
                                "Vendor Name": 9.724277560962946e-07,
                                "Vendor State": 7.157467280194396e-06,
                            },
                        },
                    ],
                }
            }
        }
    },
    "review_id": None,
}
