SERVER_TIME_SCHEMA = {
    "type": "object",
    "properties": {
        "unixtime": {
            "type": "integer"
        },
        "rfc1123": {
            "type": "string"
        }
    },
    "required": [
        "unixtime",
        "rfc1123"
    ]
}

TRADING_PAIRS = {
    "leverage": {
        "type": "object",
        "properties": {
            "XXBTZUSD": {
                "type": "object",
                "properties": {
                    "leverage_buy": {
                        "type": "array",
                        "items":
                            {
                                "type": "integer"
                            }

                    },
                    "leverage_sell": {
                        "type": "array",
                        "items":
                            {
                                "type": "integer"
                            }
                    }
                },
                "required": [
                    "leverage_buy",
                    "leverage_sell"
                ]
            }
        },
        "required": [
            "XXBTZUSD"
        ]
    }
}
# More schemas ...
