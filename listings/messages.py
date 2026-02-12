import json

response = f"```json {json.dumps(ground_truth)} ```"

messages = [{"messages": [{"role": "user",
                           "content": [{"type": "text", "text": prompt},
                                       {"type": "image", "image": image},
                                        ...
                                       ]
                           },
                          {"role": "assistent",
                           "content": [{"type": "text", "text": response}]
                           }
                          ]

            },
            ...
]