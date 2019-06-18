false = False
true = True

steps =  [
    {
      "id": "5c611fbce5378f589f77e131",
      "slug": "policy-number"
    },
    {
      "id": "5c611fbce5378fa94f77e132",
      "slug": "mobile-number"
    },
    {
      "id": "5c611fbce5378f3db177e133",
      "slug": "verify-otp"
    },
    {
      "id": "5c611fbce5378f74d977e134",
      "slug": "cust-name"
    },
    {
      "id": "5c611fbce5378f37f377e135",
      "slug": "email-id"
    },
    {
      "id": "5c611fbce5378f22e777e136",
      "slug": "services"
    },
    {
      "id": "5c611fbce5378feaf077e13f",
      "slug": "change-title"
    },
    {
      "id": "5c611fbce5378f560677e137",
      "slug": "change-email-id"
    },
    {
      "id": "5c611fbce5378f71f177e138",
      "slug": "change-alternate-email-id"
    },
    {
      "id": "5c65044934b4410e1026b5af",
      "slug": "change-pincode"
    },
    {
      "id": "5c65047934b441eafa26b5b0",
      "slug": "change-address"
    },
    {
      "id": "5c611fbce5378f368977e139",
      "slug": "change-marital-status"
    },
    {
      "id": "5c611fbce5378f75f477e13a",
      "slug": "change-occupation"
    },
    {
      "id": "5c611fbce5378f90a377e13b",
      "slug": "change-pancard"
    },
    {
      "id": "5c611fbce5378f4e8877e13d",
      "slug": "change-aadhaar-number"
    },
    {
      "id": "5c611fbce5378f26f277e13c",
      "slug": "change-contact-number"
    },
    {
      "id": "5c611fbce5378f87dd77e13e",
      "slug": "change-vehicle-number"
    }
  ]
stepObj = [
        {
          "_id": "5c611fbce5378f13a377e0d5",
          "createdDate": "2018-07-25T17:43:15.783Z",
          "updatedDate": "2018-11-28T17:19:05.558Z",
          "deleted": false,
          "slug": "lead-number",
          "defaultStep": false,
          "name": "Lead Number",
          "description": "Lead number generated from inspection request",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f914877e0c7",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please share the Lead No. Provided to you."
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "कृपया आपको दी गयी लीड  संख्या एंटर करे "
                  ]
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "leadNumberValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I'm waiting for the lead number provided by us."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! मैं हमारे द्वारा प्रदान की गई लीड संख्या की प्रतीक्षा कर रहा हूं"
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Welcome!"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "यह मेरा सौभाग्य है"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I can check the status of your preinspection with your lead number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं आपके लीड नंबर के साथ आपके प्रेइंस्पेक्शन स्टेटस की स्थिति की जांच कर सकती हूं।"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Lead number is what will be given to you when you intimated your claim. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "जब आप अपने क्लेम को सूचित करते हैं तो लीड नंबर आपको दिया जाएगा।"
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Please share the Lead No. Provided to you."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "कृपया आपको दी गयी लीड  संख्या एंटर करे "
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I know you are impatient but could please mention your name"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे पता है कि आपको जल्दी है लेकिन कृपया अपना नाम बताएं "
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay, I'm waiting."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है मैं इंतज़ार कर रही हु"
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है मैं इंतज़ार कर रही हु"
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I can only check your preinspection status if I have your lead number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं आपके लीड नंबर के साथ आपके प्रेइंस्पेक्शन स्टेटस की स्थिति की जांच कर सकती हूं।"
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "All I need is your lead number to get your preinspection status."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं आपके लीड नंबर के साथ आपके प्रेइंस्पेक्शन स्टेटस की स्थिति की जांच कर सकती हूं।"
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Once I get your lead number I'll be able to get your status."
                ]
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA  AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378fac6e77e0fe",
          "createdDate": "2018-11-15T09:56:54.969Z",
          "updatedDate": "2018-11-26T18:43:47.363Z",
          "deleted": false,
          "slug": "loss-state",
          "defaultStep": false,
          "name": "loss state",
          "description": "Name of the state where vehicle is lost",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "In which state did the accident happen?"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "किस राज्य में एक्सीडेंट हुई थी ?\n\n"
                  ]
                }
              }
            }
          ],
          "autoComplete": "stateAutoComplete",
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "stateValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f8f2177e0e3",
          "createdDate": "2018-07-25T17:55:15.136Z",
          "updatedDate": "2019-01-25T12:04:50.427Z",
          "deleted": false,
          "slug": "customer-name",
          "defaultStep": false,
          "name": "Customer Name",
          "description": "Name of customer",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f52f877e0cc",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Okay, I shall immediately assist you with your query."
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "ठीक है, मैं तुरंत आपकी क्वेरी में आपकी मदद करूंगी | "
                  ]
                }
              }
            },
            {
              "type": "func",
              "id": 1,
              "func": "custNameQF"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I'm still waiting for your name."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! मैं अभी भी आपके नाम का इन्तजार कर रही  हूँ।"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I think it's a good start by knowing each other. I'm Tara and what's your name?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "चलिए, एक दूसरे को जानने से शुरुआत करते हैं । मैं तारा हूँ और आपका नाम क्या है?"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Name is a name. It can be any name. Commonly it is what people call you by."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नाम तो बस नाम होता है। यह कुछ भी हो सकता है| यह आमतौर पर वो  होता है जिससे लोग आपको बुलाते हैं ।"
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "custNameQF"
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I know you are impatient but could please mention your name, so that I can resolve your problem."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे पता है कि आपको जल्दी है लेकिन कृपया अपना नाम बताएँ , जिससे मैं आपकी समस्या का हल निकाल सकूँ | "
                    ]
                  }
                }
              }
            ],
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I don't think I understood that one. Can you rephrase for me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे नहीं लगता है कि मुझे ये समझ आया है| क्या आप दोबारा बता सकते हैं?"
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.. I'm waiting!"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है, मैं इंतज़ार कर रही हूँ।"
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Uh-oh! I really need your name to proceed further with getting your renewal notice copy."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ओह! आपकी रिन्यूअल नोटिस की कॉपी निकालने के लिए मुझे वास्तव में आपके नाम की ज़रूरत होगी|  "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Oh. Really sad not to help you. Anyways, if you need anything else, I'll always be here."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ओह| आपको बेहतर सेवा न दे पाने का मुझे दुःख है। अगर आपको कुछ और मदद चाहिए तो मैं हमेशा तैयार हूँ।"
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की  डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Waiting for your name"
                ]
              }
            ]
          },
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nameValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378fde3077e0e0",
          "createdDate": "2018-07-25T14:06:20.777Z",
          "updatedDate": "2018-12-06T06:31:21.889Z",
          "deleted": false,
          "slug": "cust-name",
          "defaultStep": false,
          "name": "Cust Name",
          "description": "Name of customer",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fdfb077e0c4",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 1,
              "messages": [
                "It seems you need a soft copy of your Renewal Notice. I will surely assist you with your request."
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 1,
                  "messages": [
                    ""
                  ]
                }
              }
            },
            {
              "type": "func",
              "id": 0,
              "func": "custNameQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nameValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I would need your name to get soft copy of your Policy."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! आपकी पॉलिसी की सॉफ्ट कॉपी निकालने के लिए मुझे आपके नाम की ज़रूरत होगी।\n"
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hmm."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "हम्म।"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I need your name to get you the policy soft copy."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपकी पॉलिसी की सॉफ्ट कॉपी आपको देने के लिए मुझे आपके नाम की ज़रूरत होगी । "
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I am just asking your name to get you the policy soft copy"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं सिर्फ पॉलिसी की सॉफ्ट कॉपी आपको देने के लिए आपका नाम पूछ रहीं हूँ"
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर।"
                    ]
                  }
                }
              },
              {
                "type": "text",
                "id": 1,
                "messages": [
                  "Could you please share your name to get policy soft copy."
                ]
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I know you are impatient but could please mention your name"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे पता है कि आपको जल्दी है लेकिन कृपया अपना नाम बताएं "
                    ]
                  }
                }
              }
            ],
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay. But I need your name to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है। लेकिन आगे बढ़ने के लिए मुझे आपके नाम की ज़रूरत होगी "
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Thank you. Could you please share your name?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "धन्यवाद। क्या आप अपना नाम बता सकते हैं ?"
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay, But I need your name to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है, लेकिन आगे बढ़ने के लिए मुझे आपके नाम की ज़रूरत होगी "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Bye.",
                  "Thank you.",
                  "Nice talking to you.",
                  "See you later.",
                  "Hope to see you soon."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "अलविदा/बाय।",
                      "धन्यवाद।",
                      "आपसे बात करके अच्छा लगा।",
                      "फिर मिलेंगे ",
                      "आशा है आपसे जल्दी मिलेंगे।"
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Now."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "अभी"
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं टाटा AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "how": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "क्या आप अपना नाम बता सकते हैं ?"
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.",
                  "Take your own time."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर।",
                      "आप आराम से समय लीजिए "
                    ]
                  }
                }
              }
            ],
            "help": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure, Please provide your name so that we can proceed further to get you the policy soft copy."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर, कृपया अपना नाम बताएं ताकि हम आगे बढ़ सकें और आपकी पॉलिसी की सॉफ्ट कॉपी आपको दे सकें "
                    ]
                  }
                }
              }
            ],
            "where": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Here."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "यहाँ।"
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Its my pleasure.",
                  "You are welcome"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ये मेरे लिए ख़ुशी की बात है ",
                      "आपका स्वागत है"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378feb9d77e0d8",
          "createdDate": "2018-07-25T17:17:42.278Z",
          "updatedDate": "2018-11-26T17:00:36.665Z",
          "deleted": false,
          "slug": "vehicle-model",
          "defaultStep": false,
          "name": "Vehicle Model",
          "description": "Vehicle model (from auto complete only)",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please select the Vehicle Model from the auto complete list."
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "ऑटो कम्पलीट लिस्ट में से वाहन का मॉडल चुनें।"
                  ]
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "vehicleModleValidator"
            }
          ],
          "autoComplete": "vehicleModelAutoComplete",
          "responses": {
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f5e8a77e0f7",
          "createdDate": "2018-08-15T13:36:22.532Z",
          "updatedDate": "2018-11-26T14:59:34.789Z",
          "deleted": false,
          "slug": "mobile-number",
          "defaultStep": false,
          "name": "Mobile Number",
          "description": "Asking for mobile number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f440077e0ca",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileQf"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I am waiting for mobile number. But if you need anything else let me know"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! मैं मोबाइल नंबर का इन्तजार कर रही हूँ । लेकिन अगर आपको कुछ और मदद चाहिए तो मुझे बताएँ।"
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You are welcome! But I am waiting for your mobile number . "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है! लेकिन मैं आपके मोबाइल नंबर का इन्तजार कर रही हूँ।"
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "We would be verifying your mobile number with your policy. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "हम आपके मोबाइल नंबर को आपकी पॉलिसी से वेरीफाई करेंगे।"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "A mobile number is a telephone number. Except it is mobile. And also, it will be 10 digits."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मोबाइल नंबर एक टेलीफोन नंबर होता है। फर्क सिर्फ इतना है कि यह मोबाइल होता है और  10 अंको का होता है | "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "mobileQuestionFunction"
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "No! Don't abuse me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नहीं! मुझसे बद्तमीज़ी न करें "
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure! I am waiting. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर! मैं इंतज़ार कर रही हूँ "
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure! Please provide me. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर! मुझे बताइए "
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I really need your mobile number to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आगे बढ़ने के लिए मुझे आपका मोबाइल नंबर चाहिए| "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You're almost there. Just give your mobile number and email id and I'll make your renewal request."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका काम लगभग हो गया है| बस अपना मोबाइल नंबर और ईमेल आईडी दे दीजिए और मैं आपका रिन्यूअल रिक्वेस्ट बना दूँगी | "
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की  डिजिटल सहायक हूँ। "
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f40b477e0da",
          "createdDate": "2018-07-25T17:08:31.859Z",
          "updatedDate": "2018-11-26T16:50:56.265Z",
          "deleted": false,
          "slug": "email-id",
          "defaultStep": false,
          "name": "Email ID",
          "description": "Email ID of user",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 1,
              "func": "emailQF"
            }
          ],
          "autoComplete": "emailValidator",
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I'm waiting for your mail id."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! मैं आपके मेल आईडी का इंतजार कर रही  हूँ।"
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Thanks! I'm waiting for email id"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "धन्यवाद! मैं मेल आईडी का इंतजार कर रही  हूँ।"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would need your email for further correspondence."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे आगे की जानकारी के लिए आपके ईमेल की ज़रूरत होगी।"
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "May I know your email id?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "क्या मैं आपका ईमेल आई डी जान सकती हूँ ?"
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "No! Don't abuse me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नहीं! मुझसे बद्तमीज़ी मत करिए "
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर "
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'll really need your email id to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आगे बढ़ने के लिए मुझे सही में आपके ईमेल आईडी की ज़रूरत होगी "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Oh No! Don't go away after all this."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "अरे नहीं! इतना आगे बढ़ने के बाद अभी मत जाइए ।"
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ]
          },
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "agentEmailValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f980077e0d6",
          "createdDate": "2018-11-15T09:57:10.381Z",
          "updatedDate": "2018-11-26T18:45:51.149Z",
          "deleted": false,
          "slug": "loss-district",
          "defaultStep": false,
          "name": "loss district",
          "description": "district name",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "autoComplete": "districtAutoComplete",
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "districtValidator"
            }
          ],
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "In which city did the accident happen?"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "किस शहर में एक्सीडेंट हुआ था?"
                  ]
                }
              }
            }
          ]
        },
        {
          "_id": "5c611fbce5378f3e3f77e0d7",
          "createdDate": "2018-11-15T05:40:25.060Z",
          "updatedDate": "2018-11-15T11:50:17.655Z",
          "deleted": false,
          "slug": "policy-number",
          "defaultStep": false,
          "name": "policy number",
          "description": "policy number ",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "policyNumberQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "paymentPolicyValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f52b477e0dc",
          "createdDate": "2018-07-22T21:06:33.681Z",
          "updatedDate": "2018-11-26T12:08:51.398Z",
          "deleted": false,
          "slug": "mobile-number",
          "defaultStep": false,
          "name": "Mobile number",
          "description": "Ask for mobile number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6efb77e0c3",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "mobileQF",
              "locale": {
                "hi": {
                  "type": "func",
                  "id": 0
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "mobileValidator",
              "locale": {
                "hi": {
                  "type": "func",
                  "id": 0
                }
              }
            }
          ],
          "responses": {
            "repeat": [
              {
                "type": "func",
                "id": 1,
                "func": "mobileQuestionFunction"
              }
            ],
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I am waiting for mobile number. But if you need anything else let me know"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! मैं आपके मोबाइल नंबर का इंतज़ार कर रही हूँ| लेकिन अगर आपको कुछ और चाहिए तो  मुझे बताएं ।"
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You are welcome! But I am waiting for your mobile number . "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है! लेकिन मैं आपके मोबाइल नंबर का इंतज़ार कर रहीं हूँ|"
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर|"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "We would be verifying your mobile number with your policy. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "हम आपके मोबाइल नंबर को पॉलिसी के साथ वेरीफाई करेंगे।"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "A mobile number is a telephone number. Except it is mobile. And also, it will be 10 digits."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मोबाइल नंबर एक टेलीफोन नंबर होता है। फर्क सिर्फ इतना है कि यह मोबाइल होता है और  10 अंको का होता है "
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "No! Don't abuse me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नहीं! मुझसे बद्तमीज़ी मत करिए | "
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure! I am waiting. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर! मैं इंतजार कर रही हूँ।"
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure! Please provide me. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर! कृपया मुझे दें | "
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I really need your mobile number to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आगे बढ़ने के लिए मुझे आपका मोबाइल नंबर चाहिए |  "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You're almost there. Just give your mobile number and email id and I'll get your policy document."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका काम लगभग हो गया है| बस अपना मोबाइल नंबर और ईमेल आईडी दे दीजिए और मैं आपका पॉलिसी डॉक्युमेंट निकाल लूँगी  | "
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "how": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे नहीं लगता है कि मुझे ये समझ आया है| क्या आप दोबारा लिख सकते हैं ? "
                    ]
                  }
                }
              }
            ],
            "help": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे नहीं लगता है कि मुझे ये समझ आया है| क्या आप दोबारा लिख सकते हैं ? "
                    ]
                  }
                }
              }
            ],
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे नहीं लगता है कि मुझे ये समझ आया है| क्या आप दोबारा लिख सकते हैं ?"
                    ]
                  }
                }
              }
            ],
            "where": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे नहीं लगता है कि मुझे ये समझ आया है| क्या आप दोबारा लिख सकते हैं ? "
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे नहीं लगता है कि मुझे ये समझ आया है| क्या आप दोबारा लिख सकते हैं ?"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f157077e0f9",
          "createdDate": "2018-11-15T10:23:56.672Z",
          "updatedDate": "2018-11-26T19:15:18.829Z",
          "deleted": false,
          "slug": "garage",
          "defaultStep": false,
          "name": "garage ",
          "description": "if vehicle is in garage ",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please share the name and landmark of the garage"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "कृपया गैराज का नाम और लैंडमार्क बताइए "
                  ]
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "garageValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378fda0177e0de",
          "createdDate": "2018-07-25T16:58:44.030Z",
          "updatedDate": "2018-11-26T16:29:24.417Z",
          "deleted": false,
          "slug": "check-agent",
          "defaultStep": false,
          "name": "Check Agent",
          "description": "Check if the user is an agent and validate",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please note this option is available for Tata AIG intermediary/agent ONLY."
                ],
                "options": [
                  {
                    "title": "Yes",
                    "text": "yes"
                  },
                  {
                    "title": "No",
                    "text": "no"
                  }
                ]
              },
              "filters": [],
              "locale": {
                "hi": {
                  "type": "quickReplies",
                  "id": 0,
                  "quickReplies": {
                    "title": [
                      "कृपया ध्यान दें कि यह ऑप्शन केवल टाटा  AIG मध्यस्थ / एजेंट के लिए ही उपलब्ध है।"
                    ],
                    "options": [
                      {
                        "title": "हाँ",
                        "text": "yes"
                      },
                      {
                        "title": " नहीं",
                        "text": "no"
                      }
                    ]
                  }
                }
              }
            }
          ],
          "responses": {
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की  डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hi. Please note this option is for TATA AIG agents only."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "कृपया ध्यान दें कि यह ऑप्शन केवल टाटा  AIG मध्यस्थ / एजेंट के लिए ही उपलब्ध है।"
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You're welcome."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है !"
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है | "
                    ]
                  }
                }
              }
            ]
          },
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "checkAgentValidator"
            }
          ],
          "autoComplete": "vehicleMakeAutoComplete"
        },
        {
          "_id": "5c611fbce5378f543377e0eb",
          "createdDate": "2018-08-15T13:36:05.979Z",
          "updatedDate": "2018-11-26T14:50:28.435Z",
          "deleted": false,
          "slug": "policy-number",
          "defaultStep": false,
          "name": "Policy Number",
          "description": "Asking for policy number\n",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f440077e0ca",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "policyNumberQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "paymentPolicyValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hey, Could you please share your policy number.",
                  "Hello, Could you please share your policy number.",
                  "Hi there, Could you please share your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्ते! कृपया क्या आप अपना पॉलिसी नंबर बता सकते हैं ।",
                      "नमस्कार! कृपया क्या आप अपना पॉलिसी नंबर बता सकते हैं ।",
                      "हाय! कृपया क्या आप अपना पॉलिसी नंबर बता सकते हैं ।"
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You are welcome."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है।"
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hmm. Could you please provide me your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "हम्म। कृपया क्या आप  मुझे अपना पॉलिसी नंबर बता सकते हैं।"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "For policy renewal, I need your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "पॉलिसी रिन्यूअल के लिए मुझे आपके पॉलिसी नंबर की ज़रूरत है "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure, I need your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर, मुझे आपका पॉलिसी नंबर चाहिए | "
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I am Tara,  I am Tata AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं तारा हूँ। मैं TATA AIG की  डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sorry for the inconvenience, Could you please provide your policy number so that we can renew your policy"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "परेशानी के लिए माफ़ी चाहूँगी, क्या आप कृपया अपना पॉलिसी नंबर दे सकते हैं ताकि हम आपकी पॉलिसी रिन्यू कर सकें।"
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.",
                  "Take your own time."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "\"ज़रूर।\"\n ",
                      "आराम से समय लीजिए"
                    ]
                  }
                }
              }
            ],
            "help": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I will surely help you, but i need your policy number to proceed."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं आपकी मदद ज़रूर करुँगी, लेकिन आगे बढ़ने के लिए मुझे आपकी पॉलिसी नंबर की ज़रूरत होगी ।"
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Could you please provide me your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "कृपया, क्या आप मुझे अपना  पॉलिसी नंबर दे सकते हैं?"
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sorry. I will not be able to proceed further with out your policy number. Could you please share your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "माफ़ कीजिए। मैं आपके पॉलिसी नंबर के बिना आगे नहीं बढ़ सकती हूँ। क्या आप कृपया अपना पॉलिसी नंबर बता सकते हैं।"
                    ]
                  }
                }
              }
            ],
            "where": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You can find your policy number in your policy documents."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आप अपना पॉलिसी नंबर अपने पॉलिसी डॉक्युमेंट्स में पा सकते हैं।"
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "If possible now, or else i will wait for you."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "हो सके तो अभी,  नहीं तो मैं इंतज़ार कर लूँगी |  "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sorry I was not able to help. You can message me anytime."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "माफ़ कीजिए मैं मदद नहीं कर पायी। आप मुझे कभी भी मैसेज कर सकते हैं।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f1b0977e0f4",
          "createdDate": "2018-07-22T20:57:59.967Z",
          "updatedDate": "2018-11-26T05:35:59.905Z",
          "deleted": false,
          "slug": "policy-number",
          "defaultStep": false,
          "name": "Policy number",
          "description": "Asking for policy number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6efb77e0c3",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "policyNumberQF",
              "locale": {
                "hi": {
                  "type": "func",
                  "id": 0
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "policyNumberValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hey, Could you please share your policy number.",
                  "Hello, Could you please share your policy number.",
                  "Hi there, Could you please share your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "कृपया क्या आप अपना पॉलिसी नंबर बता सकते हैं।",
                      "नमस्कार! क्या आप अपना पॉलिसी नंबर बता सकते हैं ।",
                      "नमस्ते, क्या आप अपना पॉलिसी नंबर बता सकते हैं| "
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You are welcome.",
                  "Its my pleasure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है।",
                      "ये मेरे लिए ख़ुशी की बात है | "
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hmm. Could you please provide me your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "हम्म। क्या आप कृपया मुझे अपना पॉलिसी नंबर दे सकते हैं।"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "To get you the policy soft copy, I need your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपकी पॉलिसी की सॉफ्ट कॉपी आपको देने के लिए मुझे आपके पॉलिसी नंबर की ज़रूरत होगी  "
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे ये ठीक से समझ नहीं आया है| क्या आप इसे दोबारा लिख सकते हैं| "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure, I need your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर, मुझे आपका पॉलिसी नंबर चाहिए | "
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sorry for the inconvenience, Could you please provide your policy number so that we will get you the policy soft copy."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "परेशानी के लिए माफ़ी चाहूँगी, क्या आप कृपया अपना पॉलिसी नंबर दे सकते हैं ताकि हम आपको पॉलिसी की सॉफ्ट कॉपी दे सकें।"
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.",
                  "Take your own time."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर।",
                      "आप ज़रूरी समय ले सकते हैं |"
                    ]
                  }
                }
              }
            ],
            "help": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I will surely help you, but i need your policy number to proceed."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं आपकी मदद ज़रूर करुँगी, लेकिन आगे बढ़ने के लिए मुझे आपका पॉलिसी नंबर चाहिए | "
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.",
                  "Could you please provide me your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है।",
                      "क्या आप कृपया मुझे अपना पॉलिसी नंबर दे सकते हैं।"
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sorry. I will not be able to proceed further with out your policy number. Could you please share your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "माफ़ कीजिए। मैं आपके पॉलिसी नंबर के बिना आगे नहीं बढ़ सकती हूँ। क्या आप कृपया अपना पॉलिसी नंबर बता सकते हैं।"
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Bye.",
                  "Thank you.",
                  "Nice talking to you.",
                  "See you later.",
                  "Hope to see you soon."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "अलविदा/बाय।",
                      "धन्यवाद।",
                      "आपसे बात करके अच्छा लगा।",
                      "फिर मिलेंगे ",
                      "आशा है, आप जल्दी ही हमें सेवा का मौका देंगे।"
                    ]
                  }
                }
              }
            ],
            "where": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You can find your policy number in your policy documents."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपको अपना पॉलिसी नंबर अपने पॉलिसी डॉक्युमेंट्स में मिल जाएगा|"
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "If possible now, or else i will wait for you."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "हो सके तो अभी नहीं तो मैं इंतज़ार कर सकती हूँ "
                    ]
                  }
                }
              }
            ],
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm sorry but I need your policy number to proceed. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "माफ़ कीजिए, लेकिन आगे बढ़ने के लिए मुझे आपका पॉलिसी नंबर चाहिए | "
                    ]
                  }
                }
              }
            ],
            "how": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे नहीं लगता है कि मुझे ये समझ आया है| क्या आप दोबारा लिख सकते हैं | "
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378ff19277e106",
          "createdDate": "2018-07-25T17:20:47.435Z",
          "updatedDate": "2018-11-26T17:04:10.251Z",
          "deleted": false,
          "slug": "registration-number",
          "defaultStep": false,
          "name": "Registration number",
          "description": "Vehicle registration number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please share the Vehicle Registration No.\n(for eg. MH 00 AB 0000)"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "कृपया वाहन रजिस्ट्रेशन नंबर बताए (उदाहरण: MH 00 AB 0000)"
                  ]
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "registrationNumberValidator"
            }
          ],
          "responses": {
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f06d177e0ea",
          "createdDate": "2018-07-25T15:41:57.647Z",
          "updatedDate": "2018-12-10T09:00:08.673Z",
          "deleted": false,
          "slug": "email",
          "defaultStep": false,
          "name": "Email",
          "description": "Email of user",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "claimEmailQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "emailValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I would need your email id to make your claim"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! मुझे आपका क्लेम करने  के लिए आपके ईमेल आईडी की ज़रूरत होगी।"
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Welcome!"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है!"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I  would need your email id to make your claim"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे क्लेम करने के लिए आपके ईमेल आईडी की ज़रूरत होगी।"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You ask what's email ? It's a fancy little thing by which people send and receive mails. Over the internet.! Fancy stuff if you ask me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      " क्या आप जानना चाहते हैं कि ईमेल क्या होता है? ये एक छोटी सी शानदार चीज़ है जिससे लोग सन्देश भेजते और पाते हैं; वो भी इंटरनेट पर | मेरी माने तो ये काफी आधुनिक है| "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "emailQuestionFunction"
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "😱😱"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "😱😱"
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.! I'll wait."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है।! मैं इंतजार करुँगी।"
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर "
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I really need your email to make your claim"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "क्लेम बनाने के लिए मुझे वास्तव में आपके ईमेल आईडी की ज़रूरत होगी।"
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Uh-Noo. You're almost there. Just give your email id and I'll make your claim right away."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ओह! आपका काम लगभग हो गया है| बस अपना ईमेल आईडी दें और मैं आपका क्लेम अभी कर  देती हूँ| "
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'll be making your claim as soon as you tell me your mail id"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "जैसे ही आप मुझे अपना मेल आईडी देते हैं , मैं आपका क्लेम कर दूंगी ।"
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं तारा हूँ। मैं TATA AIG की  डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f4a9077e0ef",
          "createdDate": "2018-07-25T17:38:51.144Z",
          "updatedDate": "2018-11-26T17:20:50.060Z",
          "deleted": false,
          "slug": "pincode",
          "defaultStep": false,
          "name": "Pincode",
          "description": "Pincode of place",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please enter the pincode"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "कृपया पिनकोड डालें "
                  ]
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "pincodeValidator",
              "filters": []
            }
          ],
          "responses": {
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378fec6f77e0f3",
          "createdDate": "2018-11-13T11:53:16.705Z",
          "updatedDate": "2018-11-13T12:17:37.478Z",
          "deleted": false,
          "slug": "select-language",
          "defaultStep": false,
          "name": "select language",
          "description": "Select the language you want to change to ",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6b6477e0cf",
          "__v": 0,
          "validators": [],
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please let me know the language you are comfortable in and I'll change my language to your preferred language"
                ],
                "options": [
                  {
                    "title": "English",
                    "text": "change my language to english"
                  },
                  {
                    "title": "Hindi",
                    "text": "Change my language to hindi"
                  }
                ]
              }
            }
          ]
        },
        {
          "_id": "5c611fbce5378f6fe177e0f5",
          "createdDate": "2018-11-15T10:23:26.220Z",
          "updatedDate": "2018-11-26T19:18:23.676Z",
          "deleted": false,
          "slug": "cur-landmark",
          "defaultStep": false,
          "name": "cur landmark",
          "description": "current land mark ",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please share Landmark for the location along with pin code where the vehicle is?"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "कृपया जहां वाहन है  उस जगह का लैंडमार्क पिन कोड सहित बताइए "
                  ]
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "claimCurrentLandmardValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f1cac77e0fb",
          "createdDate": "2018-07-25T17:41:25.707Z",
          "updatedDate": "2018-11-26T17:36:18.927Z",
          "deleted": false,
          "slug": "insured-mobile-number",
          "defaultStep": false,
          "name": "Insured Mobile Number",
          "description": "Mobile number of insured",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "May I know the mobile no. of the insured?"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "क्या मैं  इंश्योर्ड व्यक्ति का मोबाइल नंबर जान सकती हूँ?"
                  ]
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "insuredNamePhone"
            }
          ],
          "responses": {
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।\n"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f0cb177e104",
          "createdDate": "2018-07-25T17:52:26.389Z",
          "updatedDate": "2019-01-25T13:24:06.193Z",
          "deleted": false,
          "slug": "customer-name",
          "defaultStep": false,
          "name": "Customer Name",
          "description": "Name of customer",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f343c77e0c9",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "custNameQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nameValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! May I know your name please."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! आपकी पॉलिसी की सॉफ्ट कॉपी निकालने के लिए मुझे आपके नाम की ज़रूरत होगी।\n"
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hmm."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "हम्म।"
                    ]
                  }
                }
              },
              {
                "type": "text",
                "id": 1,
                "messages": [
                  "Could you please share your name so that we can proceed."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 1,
                    "messages": [
                      "क्या आप अपना नाम बता सकते हैं ?"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would need your name so that our agents can server you better."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपकी पॉलिसी की सॉफ्ट कॉपी आपको देने के लिए मुझे आपके नाम की ज़रूरत होगी । "
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I am just asking your name to connect you to our support team"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं सिर्फ पॉलिसी की सॉफ्ट कॉपी आपको देने के लिए आपका नाम पूछ रहीं हूँ"
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "custNameQF"
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I know you are impatient but could please mention your name"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे पता है कि आपको जल्दी है लेकिन कृपया अपना नाम बताएं "
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर।"
                    ]
                  }
                }
              }
            ],
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay. But I need your name to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है। लेकिन आगे बढ़ने के लिए मुझे आपके नाम की ज़रूरत होगी "
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Thank you. Could you please share your name?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "धन्यवाद। क्या आप अपना नाम बता सकते हैं ?"
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay, But I need your name to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है, लेकिन आगे बढ़ने के लिए मुझे आपके नाम की ज़रूरत होगी "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Bye.",
                  "See you.",
                  "It was nice talking to you."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "अलविदा/बाय",
                      "फिर मिलेंगे ",
                      "आप से बात कर के अच्छा लगा।"
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं टाटा AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Its my pleasure.",
                  "You are welcome"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ये मेरे लिए ख़ुशी की बात है ",
                      "आपका स्वागत है"
                    ]
                  }
                }
              }
            ],
            "how": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "क्या आप अपना नाम बता सकते हैं ?"
                    ]
                  }
                }
              }
            ],
            "help": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure, Please provide your name so that we can proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर, कृपया अपना नाम बताएं ताकि हम आगे बढ़ सकें और आपकी पॉलिसी की सॉफ्ट कॉपी आपको दे सकें "
                    ]
                  }
                }
              }
            ],
            "where": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Here."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "यहाँ।"
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Now."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "अभी"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f2afb77e109",
          "createdDate": "2018-11-15T10:19:45.166Z",
          "updatedDate": "2018-11-15T12:12:50.803Z",
          "deleted": false,
          "slug": "license-no",
          "defaultStep": false,
          "name": "License no",
          "description": "license no of the driver",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "licenceNoQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "licenceValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f6b4e77e113",
          "createdDate": "2018-07-25T17:09:40.201Z",
          "updatedDate": "2018-11-26T16:55:53.979Z",
          "deleted": false,
          "slug": "vehicle-type",
          "defaultStep": false,
          "name": "Vehicle Type",
          "description": "Type of vehicle",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "May I know the type of Vehicle? Please select from the options."
                ],
                "options": [
                  {
                    "title": "Private Car",
                    "text": "Pvt. Car$6"
                  },
                  {
                    "title": "Two Wheeler",
                    "text": "Two-Wheeler$4"
                  },
                  {
                    "title": "Passenger Carrying Vehicle",
                    "text": "PCV$7"
                  },
                  {
                    "title": "Goods Carrying Vehicle",
                    "text": "GCV$2"
                  },
                  {
                    "title": "Miscellaneous",
                    "text": "Misellaneous Vehicle$10"
                  }
                ]
              },
              "locale": {
                "hi": {
                  "type": "quickReplies",
                  "id": 0,
                  "quickReplies": {
                    "title": [
                      "क्या मैं वाहन का प्रकार जान सकती हूँ? कृपया विकल्पों (ऑप्शंस) में से चुनें।"
                    ],
                    "options": [
                      {
                        "title": "Option",
                        "text": ""
                      }
                    ]
                  }
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "vehicleTypeValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hi! In case you forgot, I'm waiting for the vehicle type."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्ते! अगर आप भूल गए हैं तो , मैं वाहन के प्रकार(टाइप ) का इंतजार कर रही  हूँ।"
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Thanks!"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "धन्यवाद !"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would need your vehicle type, make, model and other details for making a preinspection request."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "प्रीइंस्पेक्शन रिक्वेस्ट करने के लिए मुझे आपके वाहन का प्रकार, मॉडल और अन्य जानकारी की ज़रूरत होगी"
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "May I know the type of Vehicle? "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "क्या मैं आपके वाहन का प्रकार(टाइप) जान सकती हूँ?"
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "No! Dont abuse me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नहीं! मुझसे बद्तमीज़ी मत करिए आगे बढ़ने के लिए मुझे वास्तव में आपके वाहन के प्रकार की ज़रूरत होगी | "
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure!"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर "
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I really need your vehicle type to go further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आगे बढ़ने के लिए मुझे वास्तव में आपके वाहन के प्रकार की ज़रूरत होगी | "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay! Bye."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है ! अलविदा | "
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f253177e0e1",
          "createdDate": "2018-11-15T09:53:54.989Z",
          "updatedDate": "2018-11-15T12:01:39.750Z",
          "deleted": false,
          "slug": "reg-no",
          "defaultStep": false,
          "name": "reg no",
          "description": "Vehicle registration number of the user",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "vechicleRegQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "regValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f547e77e0f0",
          "createdDate": "2018-11-15T09:55:04.653Z",
          "updatedDate": "2018-11-28T18:02:23.230Z",
          "deleted": false,
          "slug": "description",
          "defaultStep": false,
          "name": "description",
          "description": "Description of how the accident happend",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 1,
              "quickReplies": {
                "title": [
                  "May I know how did the accident happen? Please describe the accident."
                ],
                "options": [
                  {
                    "title": "Not aware of accident details",
                    "text": "Not aware of accident details"
                  }
                ]
              },
              "locale": {
                "hi": {
                  "type": "quickReplies",
                  "id": 1,
                  "quickReplies": {
                    "title": [
                      "क्या मैं जान सकती हूँ ये एक्सीडेंट कैसे हुआ ? कृपया एक्सीडेंट के बारे में विस्तार से बताइए | "
                    ],
                    "options": [
                      {
                        "title": "मुझे नहीं पता कि कैसे हुआ",
                        "text": "Not aware of how accident happened"
                      }
                    ]
                  }
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "claimDescriptionValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f544177e0f2",
          "createdDate": "2018-07-25T15:40:00.107Z",
          "updatedDate": "2018-11-26T18:08:31.850Z",
          "deleted": false,
          "slug": "mobile",
          "defaultStep": false,
          "name": "mobile",
          "description": "Mobile number of user",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileQf"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileValidator",
              "locale": {
                "hi": {
                  "type": "func",
                  "id": 0
                }
              }
            }
          ],
          "responses": {
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "It's quite unfortunate! But I need your mobile number to proceed"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "यह बहुत दुर्भाग्यपूर्ण है! लेकिन आगे बढ़ने के लिए मुझे आपके मोबाइल नंबर की ज़रूरत होगी "
                    ]
                  }
                }
              }
            ],
            "greeting": [
              {
                "type": "quickReplies",
                "id": 0,
                "quickReplies": {
                  "title": [
                    "Hello! I am waiting for mobile number. But if you need anything else let me know"
                  ],
                  "options": [
                    {
                      "title": "Policy Document",
                      "text": ""
                    },
                    {
                      "title": "Renewal Status/Payment",
                      "text": ""
                    }
                  ]
                },
                "locale": {
                  "hi": {
                    "type": "quickReplies",
                    "id": 0,
                    "quickReplies": {
                      "title": [
                        "नमस्कार! मैं आपके मोबाइल नंबर का इंतज़ार कर रहीं हूँ| लेकिन अगर आपको कुछ और चाहिए तो  मुझे बताएं ।"
                      ],
                      "options": [
                        {
                          "title": "Option",
                          "text": ""
                        }
                      ]
                    }
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर "
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "We would be verifying your mobile number with your policy. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "हम आपके मोबाइल नंबर को पॉलिसी के साथ वेरीफाई करेंगे।"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "A mobile number is a telephone number. Except it is mobile. And also, it will be 10 digits."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मोबाइल नंबर एक टेलीफोन नंबर होता है। फरक सिर्फ इतना है कि यह मोबाइल होता है और हाँ यह 10 अंको का होता है \n"
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "mobileQuestionFunction"
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "No! Don't abuse me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नहीं! मुझसे बद्तमीज़ी मत करिए "
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure. I'm waiting."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है। मैं इंतज़ार कर रही हूँ।"
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure! Please provide me. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर! कृपया मुझे बताइए"
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I really need your mobile number to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आगे बढ़ने के लिए मुझे वास्तव में आपके मोबाइल नंबर की ज़रूरत होगी | "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You're almost there. Just give your mobile number and email id and I'll intimate your claim."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका काम लगभग हो गया है| बस अपना मोबाइल नंबर और ईमेल आईडी दे दीजिए और मैं आपको क्लेम की सूचना दे दूंगी| "
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं तारा हूँ। मैं TATA AIGकी  डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378fa87c77e10b",
          "createdDate": "2018-07-25T17:40:36.860Z",
          "updatedDate": "2018-11-26T17:33:54.029Z",
          "deleted": false,
          "slug": "insured-name",
          "defaultStep": false,
          "name": "Insured Name",
          "description": "Name of insured",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "May I know the full name of the insured?"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "क्या मैं  इंश्योर्ड व्यक्ति का पूरा नाम जान सकती हूँ?"
                  ]
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "insuredNameValidator"
            }
          ],
          "responses": {
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f7eff77e110",
          "createdDate": "2018-11-15T10:21:47.427Z",
          "updatedDate": "2018-11-26T18:56:55.526Z",
          "deleted": false,
          "slug": "tieup-garages",
          "defaultStep": false,
          "name": "tieup garages",
          "description": "Asking user if he wants to know about tie up garages",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Would you like to visit our tie up garages?"
                ],
                "options": [
                  {
                    "title": "Yes",
                    "text": "yes"
                  },
                  {
                    "title": "No",
                    "text": "no"
                  }
                ]
              },
              "locale": {
                "hi": {
                  "type": "quickReplies",
                  "id": 0,
                  "quickReplies": {
                    "title": [
                      "क्या आप हमारे टाइ अप गैराजों को देखना चाहेंगे ?"
                    ],
                    "options": [
                      {
                        "title": "Option",
                        "text": ""
                      }
                    ]
                  }
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "tieupGaragesValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f904177e0fa",
          "createdDate": "2018-07-25T17:32:05.798Z",
          "updatedDate": "2018-11-26T17:14:25.237Z",
          "deleted": false,
          "slug": "district",
          "defaultStep": false,
          "name": "District",
          "description": "District of inspection check",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please select the city from the auto complete list."
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "ऑटो कम्पलीट लिस्ट में से शहर चुनें।"
                  ]
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "districtValidator",
              "locale": {
                "hi": {
                  "type": "func",
                  "id": 0
                }
              }
            }
          ],
          "autoComplete": "districtAutoComplete",
          "responses": {
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f4de677e0fc",
          "createdDate": "2018-11-15T09:55:48.724Z",
          "updatedDate": "2019-01-11T11:51:10.595Z",
          "deleted": false,
          "slug": "claim-type",
          "defaultStep": false,
          "name": "claim type",
          "description": "Type of the claim vehicle damage, loss etc",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please select the appropriate option to describe your loss."
                ],
                "options": [
                  {
                    "title": "Vehicle Damage",
                    "text": "OD"
                  },
                  {
                    "title": "Key Loss",
                    "text": "Key"
                  },
                  {
                    "title": "Tyre Damage",
                    "text": "tyre"
                  },
                  {
                    "title": "Parked and Vehicle Damage",
                    "text": "parked"
                  }
                ]
              },
              "locale": {
                "hi": {
                  "type": "quickReplies",
                  "id": 0,
                  "quickReplies": {
                    "title": [
                      "कृपया सही विकल्प (ऑप्शन) चुनिए जो आपके नुकसान के बारे में बता सके |  "
                    ],
                    "options": [
                      {
                        "title": "Option",
                        "text": ""
                      }
                    ]
                  }
                }
              },
              "filters": [
                {
                  "type": "steps",
                  "step": "motor-type",
                  "operator": "!=",
                  "value": "2"
                }
              ]
            },
            {
              "type": "quickReplies",
              "id": 1,
              "quickReplies": {
                "title": [
                  "Please select the appropriate option to describe your loss."
                ],
                "options": [
                  {
                    "title": "Vehicle Damage",
                    "text": "OD"
                  },
                  {
                    "title": "Parked and Vehicle Damage",
                    "text": "parked"
                  }
                ]
              },
              "filters": [
                {
                  "type": "steps",
                  "step": "motor-type",
                  "operator": "==",
                  "value": "2"
                }
              ]
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "claimTypeValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f598577e100",
          "createdDate": "2018-07-21T18:02:35.242Z",
          "updatedDate": "2019-02-06T18:24:18.379Z",
          "deleted": false,
          "slug": "default",
          "defaultStep": true,
          "journeyId": "5c611fbce5378f1b0177e0c2",
          "name": "Default",
          "description": "This is the default step",
          "botId": "x1542952684229",
          "prompts": [
            {
              "type": "func",
              "id": 2,
              "func": "defaultValidator"
            },
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Hi. How may I assist you today?"
                ],
                "options": [
                  {
                    "title": "Policy / Renewal Document",
                    "text": "policy softcopy and renewal document",
                    "url": "",
                    "image": "https://bpvault.blob.core.windows.net/uploads/02HQvJrP2A2T1520318832459.png"
                  },
                  {
                    "title": "Renewal Status/Payment",
                    "text": "renewal request status payment",
                    "image": "https://bpvault.blob.core.windows.net/uploads/6rhhG6qGOZ2B1520318890933.png"
                  },
                  {
                    "title": "Claim Intimation",
                    "text": "claim intimation",
                    "image": "https://bpvault.blob.core.windows.net/uploads/pA6IVmE58C5u1520319042585.png"
                  },
                  {
                    "title": "Vehicle Inspection",
                    "text": "inspection",
                    "image": "https://bpvault.blob.core.windows.net/uploads/wlWF9bPHltbp1520319165318.png"
                  },
                  {
                    "title": "Buy Online",
                    "text": "buy online",
                    "image": "https://bpvault.blob.core.windows.net/uploads/OYJ7M3oDAXId1521206002664.png"
                  },
                  {
                    "title": "Others",
                    "text": "others",
                    "image": "https://bpvault.blob.core.windows.net/uploads/sZEAO5Hxa8rZ1521206204265.png"
                  },
                  {
                    "title": "General Query",
                    "text": "general enquiry"
                  }
                ]
              },
              "filters": [
                {
                  "type": "channels",
                  "channels": [
                    "yellowmessenger"
                  ]
                }
              ],
              "locale": {
                "hi": {
                  "type": "quickReplies",
                  "id": 0,
                  "quickReplies": {
                    "title": [
                      "नमस्ते! आज मई आपकी किस तरह मदद कर सकती हु "
                    ],
                    "options": [
                      {
                        "title": "Policy / Renewal Document",
                        "text": "policy softcopy and renewal document"
                      },
                      {
                        "title": "Renewal Status/Payment",
                        "text": "renewal status payment"
                      },
                      {
                        "title": "Claim Intimation",
                        "text": "claim intimation"
                      },
                      {
                        "title": "Vehicle Inspection",
                        "text": "inspection"
                      },
                      {
                        "title": "Buy Online",
                        "text": "buy online"
                      },
                      {
                        "title": "Others",
                        "text": "others"
                      }
                    ]
                  }
                }
              }
            },
            {
              "type": "quickReplies",
              "id": 2,
              "quickReplies": {
                "title": [
                  "Hi. How may I assist you today?"
                ],
                "options": [
                  {
                    "title": "Renewal Status/Payment",
                    "text": "renewal status and payment",
                    "image": "https://bpvault.blob.core.windows.net/uploads/6rhhG6qGOZ2B1520318890933.png"
                  },
                  {
                    "title": "Buy Online",
                    "text": "",
                    "image": "https://bpvault.blob.core.windows.net/uploads/OYJ7M3oDAXId1521206002664.png"
                  },
                  {
                    "title": "Others",
                    "text": "others",
                    "image": "https://bpvault.blob.core.windows.net/uploads/sZEAO5Hxa8rZ1521206204265.png"
                  },
                  {
                    "title": "General Query",
                    "text": "general enquiry"
                  }
                ]
              },
              "filters": [
                {
                  "type": "channels",
                  "channels": [
                    "alexa"
                  ]
                }
              ]
            }
          ],
          "actions": [],
          "validators": [],
          "defaultReplies": [],
          "__v": 0,
          "responses": {
            "greeting": [
              {
                "type": "quickReplies",
                "id": 0,
                "quickReplies": {
                  "title": [
                    "Hi. How may I assist you today?"
                  ],
                  "options": [
                    {
                      "title": "Policy / Renewal Document",
                      "text": "policy softcopy and renewal document",
                      "url": "",
                      "image": "https://bpvault.blob.core.windows.net/uploads/02HQvJrP2A2T1520318832459.png"
                    },
                    {
                      "title": "Renewal Status/Payment",
                      "text": "renewal request status payment",
                      "image": "https://bpvault.blob.core.windows.net/uploads/6rhhG6qGOZ2B1520318890933.png"
                    },
                    {
                      "title": "Claim Intimation",
                      "text": "claim intimation",
                      "image": "https://bpvault.blob.core.windows.net/uploads/pA6IVmE58C5u1520319042585.png"
                    },
                    {
                      "title": "Vehicle Inspection",
                      "text": "inspection",
                      "image": "https://bpvault.blob.core.windows.net/uploads/wlWF9bPHltbp1520319165318.png"
                    },
                    {
                      "title": "Buy Online",
                      "text": "buy online",
                      "image": "https://bpvault.blob.core.windows.net/uploads/OYJ7M3oDAXId1521206002664.png"
                    },
                    {
                      "title": "Others",
                      "text": "others",
                      "image": "https://bpvault.blob.core.windows.net/uploads/sZEAO5Hxa8rZ1521206204265.png"
                    },
                    {
                      "title": "General Enquiry",
                      "text": ""
                    }
                  ]
                },
                "filters": [
                  {
                    "type": "channels",
                    "channels": [
                      "yellowmessenger"
                    ]
                  }
                ],
                "locale": {
                  "hi": {
                    "type": "quickReplies",
                    "id": 0,
                    "quickReplies": {
                      "title": [
                        "नमस्ते! आज मई आपकी किस तरह मदद कर सकती हु "
                      ],
                      "options": [
                        {
                          "title": "Policy / Renewal Document",
                          "text": "policy softcopy and renewal document"
                        },
                        {
                          "title": "Renewal Status/Payment",
                          "text": "renewal status payment"
                        },
                        {
                          "title": "Claim Intimation",
                          "text": "claim intimation"
                        },
                        {
                          "title": "Vehicle Inspection",
                          "text": "inspection"
                        },
                        {
                          "title": "Buy Online",
                          "text": "buy online"
                        },
                        {
                          "title": "Others",
                          "text": "others"
                        }
                      ]
                    }
                  }
                }
              },
              {
                "type": "quickReplies",
                "id": 1,
                "quickReplies": {
                  "title": [
                    "Hi. How may I assist you today?"
                  ],
                  "options": [
                    {
                      "title": "Renewal Status/ Payment",
                      "text": "renewal status and payment"
                    },
                    {
                      "title": "Buy online",
                      "text": ""
                    },
                    {
                      "title": "Others",
                      "text": ""
                    },
                    {
                      "title": "General Enquiry",
                      "text": ""
                    }
                  ]
                },
                "filters": [
                  {
                    "type": "channels",
                    "channels": [
                      "facebook"
                    ]
                  }
                ]
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hey that's not very cool "
                ]
              }
            ],
            "help": [
              {
                "type": "quickReplies",
                "id": 0,
                "quickReplies": {
                  "title": [
                    "I can help you with the following options."
                  ],
                  "options": [
                    {
                      "title": "Policy / Renewal Document",
                      "text": "policy softcopy and renewal document",
                      "url": ""
                    },
                    {
                      "title": "Renewal Status/Payment",
                      "text": "renewal status/payment"
                    },
                    {
                      "title": "Claim Intimation",
                      "text": "claim intimation"
                    },
                    {
                      "title": "Vehicle Inspection",
                      "text": "inspection"
                    },
                    {
                      "title": "Buy Online",
                      "text": "buy online"
                    },
                    {
                      "title": "Others",
                      "text": "others"
                    }
                  ]
                },
                "filters": [
                  {
                    "type": "channels",
                    "channels": [
                      "yellowmessenger"
                    ]
                  }
                ],
                "locale": {
                  "hi": {
                    "type": "quickReplies",
                    "id": 0,
                    "quickReplies": {
                      "title": [
                        "मई आपकी इन विकल्प में सहता कर सकती हु "
                      ],
                      "options": [
                        {
                          "title": "Policy / Renewal Document",
                          "text": "policy softcopy and renewal document"
                        },
                        {
                          "title": "Renewal Status/Payment",
                          "text": "renewal status payment"
                        },
                        {
                          "title": "Claim Intimation",
                          "text": "claim intimation"
                        },
                        {
                          "title": "Vehicle Inspection",
                          "text": "inspection"
                        },
                        {
                          "title": "Buy Onine",
                          "text": "buy online"
                        },
                        {
                          "title": "Others",
                          "text": "others"
                        }
                      ]
                    }
                  }
                }
              },
              {
                "type": "quickReplies",
                "id": 1,
                "quickReplies": {
                  "title": [
                    "I can help you with the following options."
                  ],
                  "options": [
                    {
                      "title": "Renewal Status/Payment",
                      "text": "Renewal Status Payment"
                    },
                    {
                      "title": "Buy Online",
                      "text": ""
                    },
                    {
                      "title": "Others",
                      "text": "Others"
                    },
                    {
                      "title": "General Enquiry",
                      "text": ""
                    }
                  ]
                },
                "filters": [
                  {
                    "type": "channels",
                    "channels": [
                      "facebook"
                    ]
                  }
                ]
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay, Sure."
                ]
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ]
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You are welcome."
                ]
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hmm."
                ]
              }
            ],
            "why": [],
            "what": [],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Bye. Nice talking to you."
                ]
              }
            ],
            "repeat": [],
            "how": [],
            "unknown": [],
            "yes": [],
            "no": [],
            "where": [],
            "when": []
          }
        },
        {
          "_id": "5c611fbce5378fb3a177e111",
          "createdDate": "2018-11-15T10:24:14.406Z",
          "updatedDate": "2018-11-26T19:13:53.892Z",
          "deleted": false,
          "slug": "declaration",
          "defaultStep": false,
          "name": "declaration",
          "description": "declaration of the user",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "I hereby declare that the details furnished above are true and correct to the best of my knowledge and belief."
                ],
                "options": [
                  {
                    "title": "Yes",
                    "text": "yes"
                  }
                ]
              },
              "locale": {
                "hi": {
                  "type": "quickReplies",
                  "id": 0,
                  "quickReplies": {
                    "title": [
                      "मैं घोषणा करता हूँ  कि ऊपर दी गयी सारी जानकारी मेरे ज्ञान और विश्वास के हिसाब सही है  "
                    ],
                    "options": [
                      {
                        "title": "Option",
                        "text": ""
                      }
                    ]
                  }
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "declarationValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f525e77e112",
          "createdDate": "2018-07-25T17:46:14.431Z",
          "updatedDate": "2019-01-25T12:12:52.320Z",
          "deleted": false,
          "slug": "customer-name",
          "defaultStep": false,
          "name": "Customer Name",
          "description": "Name of customer",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f2e3677e0c8",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 1,
              "func": "custNameQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nameValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello again! I'm waiting for your name"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "फिर से नमस्कार! कृपया मुझे अपना नाम बताएँ| "
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I think it's a good start by knowing each other. I'm Tara and what's your name?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "चलिए, एक दूसरे को जानने से शुरुआत करते हैं । मैं तारा हूँ और आपका नाम क्या है?"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Name is a name. It can be any name. Commonly it is what people call you by."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नाम बस एक नाम है। यह कोई भी नाम हो सकता है। आमतौर यह वो होता है जिससे लोग आपको पुकारते हैं| "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "custNameQF"
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I know you are impatient but could please mention your name, so that I can resolve your problem."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे पता है कि आपको जल्दी है लेकिन कृपया अपना नाम बताएँ, ताकि मैं आपकी समस्या  का हल निकाल सकूँ| "
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Ok! I'm waiting."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है ! मैं इंतज़ार कर रही हूँ।"
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर "
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "What's there in sharing a name. I really need your name to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नाम बताने में क्या परेशानी है| आगे बढ़ने के लिए मुझे सही में आपके नाम की ज़रूरत होगी "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Oh. Really sad not to help you. Anyways, if you need anything else, I'll always be here."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ओह| आपको बेहतर सेवा न दे पाने का मुझे दुःख है। अगर आपको कुछ और मदद चाहिए तो मैं हमेशा तैयार हूँ।"
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की  डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure,"
                ]
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f720177e0e8",
          "createdDate": "2018-07-26T12:47:01.893Z",
          "updatedDate": "2018-11-26T12:22:00.589Z",
          "deleted": false,
          "slug": "email-id",
          "defaultStep": false,
          "name": "Email id",
          "description": "asking for email id",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6efb77e0c3",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "emailQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "emailValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I would need your email id to send your policy document."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! आपको रिन्यूअल नोटिस की कॉपी भेजने के लिए मुझे आपके ईमेल आईडी की ज़रुरत होगी | "
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Welcome!"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है !"
                    ]
                  }
                }
              },
              {
                "type": "quickReplies",
                "id": 1,
                "quickReplies": {
                  "title": [
                    ""
                  ],
                  "options": [
                    {
                      "title": "Option",
                      "text": ""
                    }
                  ]
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would need your email id to send your policy document."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपको रिन्यूअल नोटिस की सॉफ्ट कॉपी भेजने के लिए मुझे आपके ईमेल आईडी की ज़रुरत होगी |"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You ask what's email ? It's a fancy little thing by which people send and receive mails. Over the internet.! Fancy stuff if you ask me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      " क्या आप जानना चाहते हैं कि ईमेल क्या होता है? ये एक छोटी सी शानदार चीज़ है जिससे लोग सन्देश भेजते और पाते हैं; वो भी इंटरनेट पर | मेरी माने तो ये काफी आधुनिक है| "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "emailQF"
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "😱😱"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "😱😱"
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.! I'll wait."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है।! मैं इंतजार करुँगी।"
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ]
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I really need your email id to proceed further"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं आपके रिन्यूअल नोटिस की कॉपी और कैसे भेज सकती हूँ "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Uh-Noo. You're almost there. Just give your email id and I'll send your policy document to it right away."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ओह| आपका काम लगभग हो गया है| बस अपना ईमेल आईडी दे दीजिए और मैं आपका रिन्यूअल नोटिस तुरंत भेज दूंगी | "
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'll be sending your policy document as soon as you give me your email id."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "जैसे ही आप मुझे अपना ईमेल आईडी देते हैं, मैं आपका  रिन्यूअल नोटिस भेज दूँगी ।"
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA  AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hmm.."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ह्म्म्म।"
                    ]
                  }
                }
              }
            ],
            "how": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे नहीं लगता है कि मुझे ये समझ आया है| क्या आप दोबारा लिख सकते हैं ?"
                    ]
                  }
                }
              }
            ],
            "help": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Please contact our customer service executive to resolve your query."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "अपनी क्वेरी (सवालों) को हल करने के लिए कृपया हमारे ग्राहक सेवा कार्यकारी(कस्टमर सर्विस एग्जीक्यूटिव) से संपर्क करें।"
                    ]
                  }
                }
              }
            ],
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.. But I really need your email ID to proceed further. If you still don't have your id, please contact our customer service executive to resolve your query."
                ]
              }
            ],
            "where": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "जैसे ही आप मुझे अपना ईमेल आईडी देते हैं, मैं आपका  रिन्यूअल नोटिस भेज दूँगी ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f0b1877e0fd",
          "createdDate": "2018-07-25T17:27:33.619Z",
          "updatedDate": "2018-11-26T17:11:32.868Z",
          "deleted": false,
          "slug": "state",
          "defaultStep": false,
          "name": "State",
          "description": "State of inspection request\n",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please select the state from the auto complete list."
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "ऑटो कम्पलीट लिस्ट में से राज्य चुनें।"
                  ]
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "stateValidator"
            }
          ],
          "autoComplete": "stateAutoComplete",
          "responses": {
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f22ba77e10c",
          "createdDate": "2018-11-15T05:43:04.653Z",
          "updatedDate": "2018-11-17T07:50:57.777Z",
          "deleted": false,
          "slug": "insured-mobile",
          "defaultStep": false,
          "name": "insured mobile",
          "description": "Insured mobile number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "insuredMobile"
            }
          ],
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "claimInsuredMobileQf"
            }
          ]
        },
        {
          "_id": "5c611fbce5378fa36777e0d9",
          "createdDate": "2018-11-10T17:40:13.201Z",
          "updatedDate": "2018-11-26T19:08:01.728Z",
          "deleted": false,
          "slug": "verify-otp",
          "defaultStep": false,
          "name": "verify otp",
          "description": "Verify the otp send to registered mobile number of the user",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6efb77e0c3",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please enter the OTP send to your registered mobile number {{steps.mobile-number}}"
                ],
                "options": [
                  {
                    "title": "Resend OTP",
                    "text": "resend otp again"
                  },
                  {
                    "title": "Change Number",
                    "text": "change number"
                  }
                ]
              },
              "locale": {
                "hi": {
                  "type": "quickReplies",
                  "id": 0,
                  "quickReplies": {
                    "title": [
                      "कृपया आपके रजिस्टर्ड मोबाइल नंबर पर भेजे गए OTP को डालें {{स्टेप्स.मोबाइल नंबर}}"
                    ],
                    "options": [
                      {
                        "title": "Option",
                        "text": ""
                      },
                      {
                        "title": "Option",
                        "text": ""
                      }
                    ]
                  }
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "verifyOtp",
              "locale": {
                "hi": {
                  "type": "func",
                  "id": 0
                }
              }
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "quickReplies",
                "id": 0,
                "quickReplies": {
                  "title": [
                    ""
                  ],
                  "options": [
                    {
                      "title": "Option",
                      "text": ""
                    }
                  ]
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f263d77e0f1",
          "createdDate": "2018-07-25T17:07:27.628Z",
          "updatedDate": "2018-11-26T16:40:01.670Z",
          "deleted": false,
          "slug": "agent-mobile",
          "defaultStep": false,
          "name": "Agent Mobile",
          "description": "Mobile number of agent",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 1,
              "func": "agentMobileQf"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I'm waiting for your mobile number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! मैं आपके मोबाइल नंबर का इंतजार कर  रही  हूँ।"
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है "
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'll need your mobile number to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे आगे बढ़ने के लिए आपके मोबाइल नंबर की ज़रूरत होगी।"
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "May I have your mobile no.?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "क्या मैं आपका मोबाइल नंबर जान सकती  हूँ?"
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "No! Don't abuse me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नहीं! मुझसे बद्तमीज़ी मत करिए "
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay. I'm waiting!"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है। मैं इंतज़ार कर रही  हूँ!"
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर "
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I really need your mobile number to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे सही में आगे बढ़ने के लिए आपके मोबाइल नंबर की ज़रूरत होगी।"
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Oh no! Don't quit now."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "अरे नहीं! अभी मत जाइए  "
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f4e8e77e0dd",
          "createdDate": "2018-07-25T17:37:20.397Z",
          "updatedDate": "2018-11-26T17:18:36.795Z",
          "deleted": false,
          "slug": "place-of-inspection",
          "defaultStep": false,
          "name": "Place of inspection",
          "description": "Location of inspection",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "May I know the Street Name/Landmark where inspection is to be conducted"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "क्या मैं उस स्ट्रीट का नाम /लैंडमार्क जान सकती हूँ जहाँ इंस्पेक्शन किया जाना है"
                  ]
                }
              }
            }
          ],
          "responses": {
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ]
          },
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "addressValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378ff05177e105",
          "createdDate": "2018-11-15T10:01:03.417Z",
          "updatedDate": "2018-11-26T18:47:18.504Z",
          "deleted": false,
          "slug": "lost-city",
          "defaultStep": false,
          "name": "lost city",
          "description": "city name ",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "In which place did the accident happen?"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "किस जगह पर एक्सीडेंट हुआ था?"
                  ]
                }
              }
            }
          ],
          "autoComplete": "claimCityAutoComplete",
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "cityValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f733977e0df",
          "createdDate": "2018-11-15T10:23:05.886Z",
          "updatedDate": "2018-11-26T19:20:28.468Z",
          "deleted": false,
          "slug": "cur-city",
          "defaultStep": false,
          "name": "cur city",
          "description": "current city name",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "autoComplete": "cityAutoComplete",
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "claimCurrentCityValidator"
            }
          ],
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please select the city where the vehicle is?"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "कृपया उस शहर को चुनें जहाँ  वाहन है"
                  ]
                }
              }
            }
          ]
        },
        {
          "_id": "5c611fbce5378f0f1877e107",
          "createdDate": "2018-07-25T17:34:50.396Z",
          "updatedDate": "2018-11-26T17:16:11.575Z",
          "deleted": false,
          "slug": "city",
          "defaultStep": false,
          "name": "City",
          "description": "City of vehicle inspection",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please select the area of the inspection location."
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "कृपया इंस्पेक्टशन वाली जगह का स्थान चुनें।"
                  ]
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "cityValidator"
            }
          ],
          "autoComplete": "cityAutoComplete",
          "responses": {
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ]
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f756a77e10f",
          "createdDate": "2018-11-15T05:39:27.289Z",
          "updatedDate": "2018-11-26T17:41:44.859Z",
          "deleted": false,
          "slug": "claim-category",
          "defaultStep": false,
          "name": "claim category",
          "description": "Category of the claim motor or non motor",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "What claim would you like to intimate?"
                ],
                "options": [
                  {
                    "title": "Motor",
                    "text": "motor"
                  },
                  {
                    "title": "Non Motor",
                    "text": "non-motor"
                  }
                ]
              },
              "locale": {
                "hi": {
                  "type": "quickReplies",
                  "id": 0,
                  "quickReplies": {
                    "title": [
                      "आप क्या क्लेम  करना चाहते हैं?"
                    ],
                    "options": [
                      {
                        "title": "Option",
                        "text": ""
                      }
                    ]
                  }
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "claimValidator",
              "filters": []
            }
          ]
        },
        {
          "_id": "5c611fbce5378fda4f77e0e2",
          "createdDate": "2018-11-11T16:31:40.575Z",
          "updatedDate": "2018-11-11T16:38:53.319Z",
          "deleted": false,
          "slug": "verify-otp",
          "defaultStep": false,
          "name": "verify otp",
          "description": "otp verification for user authentication",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fdfb077e0c4",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please enter the OTP send to your mobile number {{steps.mobile-number}}"
              ]
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "verifyOtp"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f9dad77e10a",
          "createdDate": "2018-08-15T13:35:06.248Z",
          "updatedDate": "2018-11-26T14:28:32.095Z",
          "deleted": false,
          "slug": "cust-name",
          "defaultStep": false,
          "name": "Cust Name",
          "description": "Asking the name from the user\n",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f440077e0ca",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "It seems you are looking for a renewal request status/payment. I will surely assist you with your request."
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "ऐसा लगता  है कि आप रिन्यूअल रिक्वेस्ट  / पेमेंट स्टेटस जानना चाहते हैं।  मैं जरूर इसमें आपकी मदद करुँगी \n"
                  ]
                }
              }
            },
            {
              "type": "func",
              "id": 1,
              "func": "custNameQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nameValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I would need your name for your Policy renewal"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! मुझे आपकी पॉलिसी रिन्यूअल के लिए आपके नाम की ज़रूरत होगी "
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  " I would need your name for your Policy renewal"
                ]
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I am just asking your name to get you the policy soft copy"
                ]
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "custNameQF"
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I know you are impatient but could please mention your name"
                ]
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Thank you. Could you please share your name?"
                ]
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay, But I need your name to proceed further."
                ]
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Saddening to be unable to serve you better. If you need anything I'm right here to hep you"
                ]
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ]
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f7a3477e10d",
          "createdDate": "2018-07-25T17:14:08.426Z",
          "updatedDate": "2018-11-26T16:57:45.618Z",
          "deleted": false,
          "slug": "vehicle-make",
          "defaultStep": false,
          "name": "Vehicle Make",
          "description": "Vehicle Make",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please select the Vehicle Make Variant from the auto complete list."
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "ऑटो कम्पलीट लिस्ट में से वाहन का मेक वेरिएंट चुनें।"
                  ]
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "vehicleMakeValidator"
            }
          ],
          "autoComplete": "vehicleMakeAutoComplete",
          "responses": {
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f4f9377e0e6",
          "createdDate": "2018-07-25T15:39:07.966Z",
          "updatedDate": "2018-11-26T18:23:51.333Z",
          "deleted": false,
          "slug": "customer-name",
          "defaultStep": false,
          "name": "Customer name",
          "description": "Customer name",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 1,
              "func": "custNameQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nameValidator",
              "locale": {
                "hi": {
                  "type": "func",
                  "id": 0
                }
              }
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "quickReplies",
                "id": 0,
                "quickReplies": {
                  "title": [
                    "Hello again! Please provide me your name.  If you need anything else let me know"
                  ],
                  "options": [
                    {
                      "title": "Policy Document",
                      "text": ""
                    },
                    {
                      "title": "Renewal Document",
                      "text": ""
                    },
                    {
                      "title": "Renewal Status/Payment",
                      "text": ""
                    },
                    {
                      "title": "Vehicle Preinspection Request",
                      "text": ""
                    },
                    {
                      "title": "Vehicle Preinspection  Status",
                      "text": ""
                    },
                    {
                      "title": "Buy Online",
                      "text": ""
                    }
                  ]
                },
                "locale": {
                  "hi": {
                    "type": "quickReplies",
                    "id": 0,
                    "quickReplies": {
                      "title": [
                        "फिर से नमस्कार! कृपया मुझे अपना नाम बताएँ| लेकिन अगर आपको कुछ और मदद चाहिए तो मुझे बताएँ ।"
                      ],
                      "options": [
                        {
                          "title": "Option",
                          "text": ""
                        }
                      ]
                    }
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I cannot intimate your claim without your name. Can I? So I would need your name to intimate your claim."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं आपके नाम के बिना आपको क्लेम के बारे में सूचना नहीं दे सकती हूँ |  है ना ? इसलिए क्लेम की सूचना देने के लिए मुझे आपके नाम की ज़रुरत होगी | "
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Please provide me your name. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "कृपया मुझे अपना नाम बताएँ ।"
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "custNameQF"
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I know you are impatient but could please mention your name, so that I can resolve your problem."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे पता है कि आपको जल्दी है लेकिन कृपया अपना नाम बताएं , ताकि मैं आपकी समस्या को दूर कर सकूँ "
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर "
                    ]
                  }
                }
              }
            ],
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I don't think I understood that one. Can you rephrase for me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे नहीं लगता है कि मुझे ये समझ आया है| क्या आप दोबारा बता सकते हैं?"
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर "
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Uh-oh! I really need your name to proceed further with intimating your claim."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ओह हो!आगे बढ़ने और क्लेम की सूचना देने के लिए मुझे आपके नाम की ज़रुरत होगी| "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Oh. Really sad not to help you. Anyways, if you need anything else, I'll always be here."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ओह। मुझे दुःख है मैं इसमें आपकी मदद  नहीं कर सकी| कोई नहीं, अगर आपको कुछ और मदद चाहिए, तो मैं हमेशा तैयार हूँ।"
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं तारा हूँ। मैं TATA AIG की  डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Please!"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "कृपया !"
                    ]
                  }
                }
              }
            ],
            "courtesy": []
          }
        },
        {
          "_id": "5c611fbce5378fac0c77e0e7",
          "createdDate": "2018-11-15T05:39:52.497Z",
          "updatedDate": "2019-02-05T05:03:30.623Z",
          "deleted": false,
          "slug": "motor-type",
          "defaultStep": false,
          "name": "motor type",
          "description": "Type of the vehicle ",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please choose the vehicle type"
                ],
                "options": [
                  {
                    "title": "Two Wheeler",
                    "text": "2"
                  },
                  {
                    "title": "Four Wheeler",
                    "text": "4"
                  },
                  {
                    "title": "Commercial",
                    "text": "c2"
                  }
                ]
              },
              "locale": {
                "hi": {
                  "type": "quickReplies",
                  "id": 0,
                  "quickReplies": {
                    "title": [
                      "कृपया वाहन का प्रकार (टाइप) चुनें"
                    ],
                    "options": [
                      {
                        "title": "Option",
                        "text": ""
                      }
                    ]
                  }
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "motorTypeValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f803d77e0ee",
          "createdDate": "2018-08-15T13:36:43.398Z",
          "updatedDate": "2018-11-26T15:10:11.151Z",
          "deleted": false,
          "slug": "email-id",
          "defaultStep": false,
          "name": "Email id",
          "description": "Asking for email\n",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f440077e0ca",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "emailQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "emailValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I would need your email id to make your renewal request."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! आपका रिन्यूअल रिक्वेस्ट बनाने के लिए मुझे आपके ईमेल आईडी की ज़रुरत होगी  | "
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Welcome!"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है!"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would need your email id to make your renewal request."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका रिन्यूअल रिक्वेस्ट बनाने के लिए मुझे आपके ईमेल आईडी की ज़रुरत होगी  |"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You ask what's email ? It's a fancy little thing by which people send and receive mails. Over the internet.! Fancy stuff if you ask me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      " क्या आप जानना चाहते हैं कि ईमेल क्या होता है? ये एक छोटी सी शानदार चीज़ है जिससे लोग सन्देश भेजते और पाते हैं; वो भी इंटरनेट पर | मेरी माने तो ये काफी आधुनिक है| "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "emailQuestionFunction"
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "😱😱"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "😱😱"
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.! I'll wait."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है! मैं इंतजार करुँगी।"
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर | "
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I really need your email id to proceed further"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आगे बढ़ने के लिए मुझे सही में आपके ईमेल आईडी की ज़रूरत होगी "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Uh-Noo. You're almost there. Just give your email id and I'll make your renewal request right away."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "अरे, नहीं | आपका काम लगभग हो गया है| बस अपना ईमेल आईडी दें और अभी मैं आपके पॉलिसी डॉक्युमेंट उस पर भेज देती हूँ| "
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'll be making your renewal request as soon as you give me your email id."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "जैसे ही आप मुझे अपना ईमेल आईडी देते हैं, मैं आपकी रिन्यूअल रिक्वेस्ट  बना दूंगी।"
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की  डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f5d9977e10e",
          "createdDate": "2018-09-25T07:16:45.109Z",
          "updatedDate": "2018-11-26T19:06:57.269Z",
          "deleted": false,
          "slug": "doc_type",
          "defaultStep": false,
          "name": "doc_type",
          "description": "Getting the document type. Either renewal copy or new business policy document.\n",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6efb77e0c3",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Have you ever renewed this policy?"
                ],
                "options": [
                  {
                    "title": "Yes",
                    "text": "yes"
                  },
                  {
                    "title": "No",
                    "text": "no"
                  }
                ]
              },
              "locale": {
                "hi": {
                  "type": "quickReplies",
                  "id": 0,
                  "quickReplies": {
                    "title": [
                      "क्या आपने अपनी पॉलिसी रिन्यू  करवा ली है ?"
                    ],
                    "options": [
                      {
                        "title": "Option",
                        "text": ""
                      }
                    ]
                  }
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "docTypeValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I would need the policy type to get soft copy of your Policy."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार ! आपकी पॉलिसी की सॉफ्ट कॉपी निकालने के लिए मुझे पॉलिसी टाइप चाहिए | "
                    ]
                  }
                },
                "filters": [
                  {
                    "type": "custom"
                  }
                ]
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f228577e101",
          "createdDate": "2018-11-15T10:20:55.374Z",
          "updatedDate": "2018-11-26T18:53:02.943Z",
          "deleted": false,
          "slug": "garage-or-not",
          "defaultStep": false,
          "name": "garage or not",
          "description": "Location of the vehicle",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Where is your vehicle?"
                ],
                "options": [
                  {
                    "title": "Accident Location",
                    "text": "Accident Location",
                    "url": ""
                  },
                  {
                    "title": "Garage",
                    "text": "garage"
                  },
                  {
                    "title": "Other",
                    "text": "With Insured"
                  }
                ]
              },
              "locale": {
                "hi": {
                  "type": "quickReplies",
                  "id": 0,
                  "quickReplies": {
                    "title": [
                      "आपका वाहन कहाँ  है ?"
                    ],
                    "options": [
                      {
                        "title": "Option",
                        "text": ""
                      },
                      {
                        "title": "Option",
                        "text": ""
                      },
                      {
                        "title": "Option",
                        "text": ""
                      }
                    ]
                  }
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "garageOrnotValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378fdeb677e0ec",
          "createdDate": "2018-07-25T15:31:12.115Z",
          "updatedDate": "2018-11-14T11:15:45.292Z",
          "deleted": false,
          "slug": "email-id",
          "defaultStep": false,
          "name": "Email ID",
          "description": "email id",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fdfb077e0c4",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "emailQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "emailValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I would need your email id to send your renewal notice copy"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! मुझे आपके ईमेल आईडी की ज़रुरत होगी आपको रिन्यूअल नोटिस की कॉपी भेजने के लिए| "
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Welcome!"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है !"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would need your email id to send the renewal notice soft copy."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे आपके ईमेल आईडी की ज़रुरत होगी आपको रिन्यूअल नोटिस की सॉफ्ट कॉपी भेजने के लिए|"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You ask what's email ? It's a fancy little thing by which people send and receive mails. Over the internet.! Fancy stuff if you ask me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      " क्या आप जानना चाहते हैं कि ईमेल क्या होता है? ये एक छोटी से शानदार चीज़ है जिससे लोग सन्देश भेजते और पाते हैं; वो भी इंटरनेट पर | मेरी माने तो ये काफी आधुनिक है| "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "emailQF"
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "😱😱"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "😱😱"
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.! I'll wait."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है।! मैं इंतजार करुँगी।"
                    ]
                  }
                }
              }
            ],
            "yes": [],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "How else can I send your renewal notice copy."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं आपके रिन्यूअल नोटिस की कॉपी और कैसे भेज सकती हूँ "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Uh-Noo. You're almost there. Just give your email id and I'll send your renewal notice to it right away."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ओह| आपका काम लगभग हो गया है| बस अपना ईमेल आईडी दे दीजिए और मैं आपका रिन्यूअल नोटिस तुरंत भेज दूंगी | "
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'll be sending your renewal notice as soon as you give me your email id."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "जैसे ही आप मुझे अपना ईमेल आईडी देते हैं, मैं आपका  रिन्यूअल नोटिस भेज दूँगी ।"
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं टाटा AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hmm."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "हम्म।"
                    ]
                  }
                }
              }
            ],
            "how": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      ""
                    ]
                  }
                }
              }
            ],
            "help": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      ""
                    ]
                  }
                }
              }
            ],
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ]
              }
            ],
            "where": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      ""
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378fb59f77e0ed",
          "createdDate": "2018-11-15T10:22:49.293Z",
          "updatedDate": "2018-11-26T19:21:21.309Z",
          "deleted": false,
          "slug": "current-districe",
          "defaultStep": false,
          "name": "current districe",
          "description": "current district",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please select the district where the vehicle is?"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "उस जिले को चुनें जहाँ वाहन है "
                  ]
                }
              }
            }
          ],
          "autoComplete": "districtAutoComplete",
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "claimCurrentdistrictValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f3c6d77e0f6",
          "createdDate": "2018-07-25T14:13:56.107Z",
          "updatedDate": "2018-11-14T10:54:30.819Z",
          "deleted": false,
          "slug": "policy-no",
          "defaultStep": false,
          "name": "Policy No",
          "description": "Policy number ",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fdfb077e0c4",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "policyNumberQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "policyNumberValidator"
            }
          ],
          "responses": {
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर।"
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure! "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर!"
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm Sorry, But I need it. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "माफ़ कीजिए , लेकिन मुझे इसकी ज़रूरत है।"
                    ]
                  }
                }
              }
            ],
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm really sorry! But I need this information to proceed. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं माफी चाहती हूँ! लेकिन आगे बढ़ने के लिए मुझे इस जानकारी की ज़रूरत है।"
                    ]
                  }
                }
              }
            ],
            "greeting": [
              {
                "type": "quickReplies",
                "id": 0,
                "quickReplies": {
                  "title": [
                    "Hello! I am waiting for policy number. But if you need anything else let me know."
                  ],
                  "options": [
                    {
                      "title": "Policy Document",
                      "text": "policy document",
                      "url": ""
                    },
                    {
                      "title": "Renewal Document",
                      "text": "renewal document"
                    },
                    {
                      "title": "Renewal Status/Payment",
                      "text": "renewal status/payment"
                    },
                    {
                      "title": "Claim Intimation",
                      "text": "claim intimation"
                    },
                    {
                      "title": "Vehicle Preinspection Request",
                      "text": "vehicle preinspection request"
                    },
                    {
                      "title": "Vehicle Preinspection  Status",
                      "text": "vehicle preinspection status"
                    },
                    {
                      "title": "Buy Online",
                      "text": "buy online"
                    },
                    {
                      "title": "Others",
                      "text": "others"
                    }
                  ]
                },
                "filters": [],
                "locale": {
                  "hi": {
                    "type": "quickReplies",
                    "id": 0,
                    "quickReplies": {
                      "title": [
                        "नमस्कार! मैं पॉलिसी नंबर का इंतजार कर रही हूँ|  लेकिन अगर आपको कुछ और मदद चाहिए तो मुझे बातए।"
                      ],
                      "options": [
                        {
                          "title": "Policy Document",
                          "text": "policy document"
                        },
                        {
                          "title": "Preinspection Request",
                          "text": "preinspection request"
                        },
                        {
                          "title": "Renewal/Status Payment",
                          "text": "renewal status"
                        },
                        {
                          "title": "Claim Intimation",
                          "text": "claim intimation"
                        },
                        {
                          "title": "Preinspection Status",
                          "text": "preinspection status"
                        },
                        {
                          "title": "Buy Online",
                          "text": "buy online"
                        },
                        {
                          "title": "Others",
                          "text": "others"
                        }
                      ]
                    }
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "To get you the policy soft copy, I need your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपकी पॉलिसी की सॉफ्ट कॉपी आपको देने के लिए मुझे आपके पॉलिसी नंबर की ज़रूरत होगी  "
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ]
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "policyNumberQF",
                "locale": {
                  "hi": {
                    "type": "func",
                    "id": 0
                  }
                }
              }
            ],
            "how": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "The policy number will be printed on your Insurance card. Can you look at the card and give me the policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "पॉलिसी नंबर आपके इंश्योरेंस कार्ड पर प्रिंट किया गया होगा | क्या आप कार्ड में देखकर मुझे पॉलिसी नंबर बता सकते हैं।"
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "What wrong did I do.? Don't abuse a bot! All I'm trying is to help you."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैंने क्या गलत किया है ? एक बॉट से बद्तमीज़ी नहीं करें ! मैं तो बस आपकी मदद करने की कोशिश कर रही  हूँ ।"
                    ]
                  }
                }
              }
            ],
            "help": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm here to help. The policy number will be printed on the Insurance card. If you need help in something else, I suggest you contact our customer service executive."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं यहाँ आपकी मदद के लिए हूँ। पॉलिसी नंबर इंश्योरेंस कार्ड पर प्रिंट किया जाएगा। अगर आपको किसी और चीज़ में मदद की ज़रूरत है, तो मेरा सुझाव होगा कि आप हमारे ग्राहक सेवा कार्यकारी से संपर्क करें।"
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm unhappy that I can't serve you better. Anyways, If you need anything else, I'm always here."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपको बेहतर सेवा न दे पाने का मुझे दुःख है। लेकिन, अगर आपको कुछ और मदद चाहिए तो मैं हमेशा तैयार हूँ।"
                    ]
                  }
                }
              }
            ],
            "where": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Your policy number will be printed on the Insurance card."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका पॉलिसी नंबर आपके इंश्योरेंस  कार्ड पर प्रिंट किया जाएगा।"
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Um..! I need your policy number now."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      " मुझे आपका पॉलिसी नंबर अभी चाहिए "
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं टाटा AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You are welcome.",
                  "Its my pleasure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है।",
                      "ये मेरे लिए ख़ुशी की बात है "
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hmm. Could you please provide me your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "हम्म। क्या आप कृपया मुझे अपना पॉलिसी नंबर दे सकते हैं।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f1b7177e102",
          "createdDate": "2018-11-15T10:18:59.829Z",
          "updatedDate": "2018-11-26T18:49:02.581Z",
          "deleted": false,
          "slug": "loss-landmark",
          "defaultStep": false,
          "name": "loss landmark",
          "description": "land mark",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please share Landmark where the accident occurred along with the pin code"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "कृपया पिन कोड सहित उस लैंडमार्क का नाम बताइए जहाँ एक्सीडेंट हुआ था | "
                  ]
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "lossLandMarkValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f47f877e103",
          "createdDate": "2018-07-25T17:52:48.341Z",
          "updatedDate": "2019-01-25T13:25:08.752Z",
          "deleted": false,
          "slug": "mobile",
          "defaultStep": false,
          "name": "Mobile",
          "description": "Mobile number of customer",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f343c77e0c9",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileQf"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileValidator",
              "filters": []
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I'm still waiting for your mobile number."
                ]
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ]
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I want your mobile number so that we can get in contact with you if this conversation left unfinished"
                ]
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  " My masters know better. Just tell me your mobile number and I'll connect you with them."
                ]
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "mobileQuestionFunction"
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Abusing doesn't help at all. Spread love. Spread peace."
                ]
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ]
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ]
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would really need your mobile number to proceed further."
                ]
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You're so close to buying insurance online. Just you're mobile number and we will be on our way.."
                ]
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would need your mobile number now to connect with my superiors."
                ]
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ]
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f7c5077e114",
          "createdDate": "2018-07-22T20:48:47.063Z",
          "updatedDate": "2018-11-26T19:02:18.947Z",
          "deleted": false,
          "slug": "cust-name",
          "defaultStep": false,
          "name": "Cust Name",
          "description": "Asking the name from the user",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6efb77e0c3",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 1,
              "messages": [
                "It seems you need a soft copy of your policy document. I will surely assist you with your request."
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 1,
                  "messages": [
                    "ऐसा लग रहा है कि आपको अपनी पॉलिसी डॉक्युमेंट की सॉफ्ट कॉपी चाहिए। मैं आपकी इसमें ज़रूर मदद करुँगी\n"
                  ]
                },
                "ta": {
                  "type": "text",
                  "id": 1,
                  "messages": [
                    ""
                  ]
                }
              },
              "filters": []
            },
            {
              "type": "func",
              "id": 1,
              "func": "custNameQF",
              "locale": {
                "hi": {
                  "type": "func",
                  "id": 1
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nameValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I would need your name to get soft copy of your Policy."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! आपकी पॉलिसी की सॉफ्ट कॉपी निकालने के लिए मुझे आपके नाम की ज़रूरत होगी।\n"
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I know you are impatient but could please mention your name"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे पता है कि आपको जल्दी है लेकिन कृपया अपना नाम बताएं "
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hmm."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "हम्म।"
                    ]
                  }
                }
              },
              {
                "type": "text",
                "id": 1,
                "messages": [
                  "Could you please share your name so that we can proceed."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 1,
                    "messages": [
                      "क्या आप अपना नाम बता सकते हैं ?"
                    ]
                  }
                }
              }
            ],
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay. But I need your name to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है। लेकिन आगे बढ़ने के लिए मुझे आपके नाम की ज़रूरत होगी "
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I need your name to get you the policy soft copy."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपकी पॉलिसी की सॉफ्ट कॉपी आपको देने के लिए मुझे आपके नाम की ज़रूरत होगी । "
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I am just asking your name to get you the policy soft copy"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं सिर्फ पॉलिसी की सॉफ्ट कॉपी आपको देने के लिए आपका नाम पूछ रहीं हूँ"
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर।"
                    ]
                  }
                }
              },
              {
                "type": "text",
                "id": 1,
                "messages": [
                  "Could you please share your name to get policy soft copy."
                ]
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं टाटा AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर।"
                    ]
                  }
                }
              }
            ],
            "help": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure, Please provide your name so that we can proceed further to get you the policy soft copy."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर, कृपया अपना नाम बताएं ताकि हम आगे बढ़ सकें और आपकी पॉलिसी की सॉफ्ट कॉपी आपको दे सकें "
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Thank you. Could you please share your name?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "धन्यवाद। क्या आप अपना नाम बता सकते हैं ?"
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay, But I need your name to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है, लेकिन आगे बढ़ने के लिए मुझे आपके नाम की ज़रूरत होगी "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Bye.",
                  "See you.",
                  "It was nice talking to you."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "अलविदा/बाय",
                      "फिर मिलेंगे ",
                      "आप से बात कर के अच्छा लगा।"
                    ]
                  }
                }
              }
            ],
            "where": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Here."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "यहाँ।"
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Now."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "अभी"
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Its my pleasure.",
                  "You are welcome"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ये मेरे लिए ख़ुशी की बात है ",
                      "आपका स्वागत है"
                    ]
                  }
                }
              }
            ],
            "how": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे नहीं लगता है कि मुझे ये समझ आया है| क्या आप दोबारा बता सकते हैं?"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f178277e0db",
          "createdDate": "2018-07-25T14:17:05.039Z",
          "updatedDate": "2018-11-14T11:11:26.263Z",
          "deleted": false,
          "slug": "mobile-number",
          "defaultStep": false,
          "name": "Mobile Number",
          "description": "Mobile number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fdfb077e0c4",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "mobileQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "mobileValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I am waiting for mobile number. But if you need anything else let me know"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! मैं आपके मोबाइल नंबर का इंतजार कर रही हूँ। लेकिन अगर आपको कुछ और मदद  चाहिए तो मुझे बताए।"
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You are welcome! But I am waiting for your mobile number . "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है! लेकिन मैं आपके मोबाइल नंबर का इंतजार  कर रही हूँ।"
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure! Please provide me. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर! मुझे बताइए "
                    ]
                  }
                }
              }
            ],
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ]
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure! I am waiting. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर! मैं इंतजार कर रही हूँ।"
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "We would be verifying your mobile number with your policy. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "हम आपका मोबाइल नंबर आपकी पॉलिसी के साथ वेरीफाई करेंगे।"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "A mobile number is a telephone number. Except it is mobile. And also, it will be 10 digits."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मोबाइल नंबर एक टेलीफोन नंबर होता है। फरक सिर्फ इतना है कि यह मोबाइल होता है और हाँ यह 10 अंको का होता है "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "mobileQF"
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "No! Don't abuse me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नहीं! मुझसे बद्तमीज़ी मत करिए "
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I really need your mobile number to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आगे बढ़ने के लिए मुझे वास्तव में आपके मोबाइल नंबर की ज़रूरत होगी "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You're almost there. Just give your mobile number and email id and I'll get your renewal notice."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका काम लगभग हो गया है| बस अपना मोबाइल नंबर और ईमेल आईडी दे दीजिए और मैं आपका रिन्यूअल नोटिस ले आउंगी  "
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं टाटा AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "how": [],
            "help": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      ""
                    ]
                  }
                }
              }
            ],
            "where": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      ""
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "जैसे ही आप मुझे अपना ईमेल आईडी देंगे, मैं आपके पॉलिसी डॉक्युमेंट भेज दूँगी ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f301877e0e5",
          "createdDate": "2018-07-25T17:05:59.494Z",
          "updatedDate": "2018-11-28T16:59:55.427Z",
          "deleted": false,
          "slug": "agent-name",
          "defaultStep": false,
          "name": "Agent Name",
          "description": "Name of agent",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "It seems that you need to place a request for vehicle inspection. Before I proceed, May I know your name?"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "ऐसा लगता है कि आपको वाहन इंस्पेक्शन के लिए रिक्वेस्ट करने की ज़रूरत है। आगे बढ़ने से पहले, क्या मैं आपका नाम जान सकती हूँ ? "
                  ]
                }
              }
            },
            {
              "type": "func",
              "id": 1,
              "func": "custNameQF",
              "locale": {
                "hi": {
                  "type": "func",
                  "id": 1
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "agentNameValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I'm waiting for your name"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! मैं आपके नाम का इंतजार कर रही  हूँ।"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "As an intermediary, you must be knowing that I need your name to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मध्यस्थ के रूप में, आपको यह पता होगा कि आगे बढ़ने के लिए मुझे आपके नाम की ज़रूरत होगी "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "It seems that you need to place a request for vehicle inspection. Before I proceed, May I know your name?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ऐसा लगता है कि आपको वाहन इंस्पेक्शन के लिए रिक्वेस्ट करने की ज़रूरत है। आगे बढ़ने से पहले, क्या मैं आपका नाम जान सकती हूँ ? "
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Abusing doesn't help at all. Spread love. Spread peace."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "बद्तमीज़ी करने से कुछ नहीं होगा| प्यार फैलाएँ। शांति फैलाएँ। "
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर "
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर "
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I really need your name to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे आगे बढ़ने के लिए सही में आपके नाम की ज़रूरत होगी | "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay! Bye"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है ! अलविदा | "
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Its my pleasure.",
                  "You are welcome"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ये मेरे लिए ख़ुशी की बात है ",
                      "आपका स्वागत है"
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है | "
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  ""
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      ""
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f039677e0ff",
          "createdDate": "2018-11-15T05:41:03.634Z",
          "updatedDate": "2018-12-11T17:28:38.019Z",
          "deleted": false,
          "slug": "insured-person",
          "defaultStep": false,
          "name": "insured person",
          "description": "If the user is the insured person or not",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Are you the insured person?"
                ],
                "options": [
                  {
                    "title": "Yes",
                    "text": "yes"
                  },
                  {
                    "title": "No",
                    "text": "no"
                  }
                ]
              },
              "locale": {
                "hi": {
                  "type": "quickReplies",
                  "id": 0,
                  "quickReplies": {
                    "title": [
                      "क्या आप इंश्योर्ड व्यक्ति हैं ?"
                    ],
                    "options": [
                      {
                        "title": "Option",
                        "text": ""
                      }
                    ]
                  }
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "claimInsuredValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f045a77e0e4",
          "createdDate": "2018-11-15T09:56:11.060Z",
          "updatedDate": "2018-11-26T18:42:27.818Z",
          "deleted": false,
          "slug": "death-injury",
          "defaultStep": false,
          "name": "death injury",
          "description": "Is there any death injury",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Is there any Injury/Death"
                ],
                "options": [
                  {
                    "title": "Yes",
                    "text": "yes"
                  },
                  {
                    "title": "No",
                    "text": "no"
                  }
                ]
              },
              "locale": {
                "hi": {
                  "type": "quickReplies",
                  "id": 0,
                  "quickReplies": {
                    "title": [
                      "क्या कोई घायल या किसी की मृत्यु हुई है ?"
                    ],
                    "options": [
                      {
                        "title": "Option",
                        "text": ""
                      }
                    ]
                  }
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "deathInjuryValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378fc58277e0e9",
          "createdDate": "2018-11-15T10:19:16.079Z",
          "updatedDate": "2018-11-26T18:50:37.484Z",
          "deleted": false,
          "slug": "driver-name",
          "defaultStep": false,
          "name": "driver name",
          "description": "Driver name ",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please enter the name of the driver"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "कृपया ड्राइवर का नाम डालें "
                  ]
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "driverNameValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378fa2eb77e108",
          "createdDate": "2018-11-15T09:54:26.862Z",
          "updatedDate": "2018-11-15T12:03:02.172Z",
          "deleted": false,
          "slug": "accident-date-time",
          "defaultStep": false,
          "name": "accident date time",
          "description": "Get accident date time of the user",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "dateAndTimeQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "dateAndTimeValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f6dcb77e0f8",
          "createdDate": "2018-11-15T10:22:32.412Z",
          "updatedDate": "2018-12-28T08:22:57.868Z",
          "deleted": false,
          "slug": "cur-state",
          "defaultStep": false,
          "name": "cur state",
          "description": "Current state",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f6f5977e0c5",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please select the state where the vehicle is?"
              ],
              "locale": {
                "hi": {
                  "type": "text",
                  "id": 0,
                  "messages": [
                    "जहाँ वाहन है वह राज्य चुनें "
                  ]
                }
              }
            }
          ],
          "autoComplete": "stateAutoComplete",
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "claimCurrentStateValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378fee1677e12b",
          "createdDate": "2018-11-29T07:34:48.124Z",
          "updatedDate": "2018-12-03T09:07:52.687Z",
          "deleted": false,
          "slug": "wording-travel",
          "defaultStep": false,
          "name": "wording travel",
          "description": "wording_travel",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f27ec77e0d1",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please choose a Travel Insurance Product"
                ],
                "options": [
                  {
                    "title": "Travel Guard",
                    "text": "Travel Guard"
                  },
                  {
                    "title": "Student Guard Plus Policy ",
                    "text": "Student Guard Plus Policy "
                  },
                  {
                    "title": "Domestic Travel Guard Policy",
                    "text": "Domestic Travel Guard Policy"
                  },
                  {
                    "title": "Asia Travel Guard Policy",
                    "text": "Asia Travel Guard Policy"
                  }
                ]
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "wordingTravelValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f0abf77e119",
          "createdDate": "2019-01-02T12:59:11.129Z",
          "updatedDate": "2019-01-02T13:00:11.206Z",
          "deleted": false,
          "slug": "select-language",
          "defaultStep": false,
          "name": "select language",
          "description": "select language",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f52f877e0cc",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please let me know the language you are comfortable in"
                ],
                "options": [
                  {
                    "title": "English",
                    "text": "english"
                  },
                  {
                    "title": "Hindi",
                    "text": "hindi"
                  }
                ]
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "othersInit"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f22e777e136",
          "createdDate": "2019-02-09T18:34:16.662Z",
          "updatedDate": "2019-02-09T18:58:11.618Z",
          "deleted": false,
          "slug": "services",
          "defaultStep": false,
          "name": "services",
          "description": "services",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "servicesQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "servicesValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f775177e12c",
          "createdDate": "2018-11-16T07:13:48.704Z",
          "updatedDate": "2019-01-25T13:25:43.671Z",
          "deleted": false,
          "slug": "email",
          "defaultStep": false,
          "name": "email",
          "description": "Email of the user",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f343c77e0c9",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "emailQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "emailValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! Waiting for your email Id."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! आपको रिन्यूअल नोटिस की कॉपी भेजने के लिए मुझे आपके ईमेल आईडी की ज़रुरत होगी | "
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Welcome!"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है !"
                    ]
                  }
                }
              },
              {
                "type": "quickReplies",
                "id": 1,
                "quickReplies": {
                  "title": [
                    ""
                  ],
                  "options": [
                    {
                      "title": "Option",
                      "text": ""
                    }
                  ]
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hmm.."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ह्म्म्म।"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would need your email id to send you any related information to your query."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपको रिन्यूअल नोटिस की सॉफ्ट कॉपी भेजने के लिए मुझे आपके ईमेल आईडी की ज़रुरत होगी |"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You ask what's email ? It's a fancy little thing by which people send and receive mails. Over the internet.! Fancy stuff if you ask me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      " क्या आप जानना चाहते हैं कि ईमेल क्या होता है? ये एक छोटी सी शानदार चीज़ है जिससे लोग सन्देश भेजते और पाते हैं; वो भी इंटरनेट पर | मेरी माने तो ये काफी आधुनिक है| "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "emailQF"
              }
            ],
            "how": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे नहीं लगता है कि मुझे ये समझ आया है| क्या आप दोबारा लिख सकते हैं ?"
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA  AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "😱😱"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "😱😱"
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.! I'll wait."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है।! मैं इंतजार करुँगी।"
                    ]
                  }
                }
              }
            ],
            "help": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Please contact our customer service executive to resolve your query."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "अपनी क्वेरी (सवालों) को हल करने के लिए कृपया हमारे ग्राहक सेवा कार्यकारी(कस्टमर सर्विस एग्जीक्यूटिव) से संपर्क करें।"
                    ]
                  }
                }
              }
            ],
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.. But I really need your email ID to proceed further. If you still don't have your id, please contact our customer service executive to resolve your query."
                ]
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ]
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I really need your email id to proceed further"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं आपके रिन्यूअल नोटिस की कॉपी और कैसे भेज सकती हूँ "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Uh-Noo. You're almost there. Just give your email id and I'll connect you with our agent  right away."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ओह| आपका काम लगभग हो गया है| बस अपना ईमेल आईडी दे दीजिए और मैं आपका रिन्यूअल नोटिस तुरंत भेज दूंगी | "
                    ]
                  }
                }
              }
            ],
            "where": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "जैसे ही आप मुझे अपना ईमेल आईडी देते हैं, मैं आपका  रिन्यूअल नोटिस भेज दूँगी ।"
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'll be connecting you as soon as you give me your email id."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "जैसे ही आप मुझे अपना ईमेल आईडी देते हैं, मैं आपका  रिन्यूअल नोटिस भेज दूँगी ।"
                    ]
                  }
                }
              }
            ],
            "ZX": []
          }
        },
        {
          "_id": "5c611fbce5378f5bfa77e11c",
          "createdDate": "2018-11-29T07:34:25.760Z",
          "updatedDate": "2018-12-03T10:11:02.761Z",
          "deleted": false,
          "slug": "brochure-health",
          "defaultStep": false,
          "name": "brochure health",
          "description": "brochure_health\n",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f27ec77e0d1",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please choose a Health and Accident Insurance Product"
                ],
                "options": [
                  {
                    "title": "Individual Accident & Sickness Policy ",
                    "text": "individual_accident"
                  },
                  {
                    "title": "MediPrime",
                    "text": "MediPrime"
                  },
                  {
                    "title": "MediPlus",
                    "text": "MediPlus"
                  },
                  {
                    "title": "Medisenior",
                    "text": "Medisenior"
                  },
                  {
                    "title": "Hospital Cash Policy ",
                    "text": "hospital_cash"
                  },
                  {
                    "title": "Wellsurance Family Policy",
                    "text": "wellsurance_family"
                  },
                  {
                    "title": "Wellsurance Woman Policy",
                    "text": "wellsurance_woman"
                  },
                  {
                    "title": "Wellsurance Executive Policy",
                    "text": "wellsurance_executive"
                  },
                  {
                    "title": "MediRaksha",
                    "text": "MediRaksha"
                  }
                ]
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "brochureHealthValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f0d4f77e11e",
          "createdDate": "2019-01-22T08:27:45.296Z",
          "updatedDate": "2019-01-22T08:29:38.618Z",
          "deleted": false,
          "slug": "policy-number",
          "defaultStep": false,
          "name": "policy number",
          "description": "policy number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f52f877e0cc",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Okay, I shall immediately assist you with your query."
              ]
            },
            {
              "type": "func",
              "id": 1,
              "func": "othersPolicyNumberQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "othersPolicyValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f308c77e11a",
          "createdDate": "2018-12-04T06:38:37.083Z",
          "updatedDate": "2018-12-04T06:56:43.331Z",
          "deleted": false,
          "slug": "type",
          "defaultStep": false,
          "name": "type",
          "description": "type of location",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f996377e0d2",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please choose the type of service you want"
                ],
                "options": [
                  {
                    "title": "Garages",
                    "text": "garages"
                  },
                  {
                    "title": "Hospitals",
                    "text": "hospitals"
                  },
                  {
                    "title": "Branches",
                    "text": "branches"
                  }
                ]
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "tieUpTypeValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f07de77e115",
          "createdDate": "2018-11-29T07:31:57.470Z",
          "updatedDate": "2018-12-20T18:44:07.767Z",
          "deleted": false,
          "slug": "mobile-number",
          "defaultStep": false,
          "name": "mobile number",
          "description": "mobile number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f27ec77e0d1",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileQf"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello again! I'm still waiting for your mobile number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "फिर से नमस्कार! मैं अभी भी आपके मोबाइल नंबर का इंतज़ार कर रही  हूँ।"
                    ]
                  }
                }
              }
            ],
            "courtesy": [],
            "okay": [],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "To help you better, I would require your mobile number"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं आपका मोबाइल नंबर उसी लिए मांग रही हूँ जिसके लिए सब मांगते हैं| "
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  " My masters know better. Just tell me your mobile number and I'll connect you with them."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरे मास्टर्स ज्यादा बेहतर जानते हैं। अपना मोबाइल नंबर बताइए मैं आपको उनसे कनेक्ट कर देती हूँ | "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "mobileQuestionFunction"
              }
            ],
            "how": [],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की  डिजिटल सहायक हूँ। "
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Abusing doesn't help at all. Spread love. Spread peace. And tell me your mobile number if you want to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "बद्तमीज़ी करने से कुछ नहीं होगा| प्यार फैलाएँ। और अपना मोबाइल नंबर बताएँ अगर आगे बढ़ना चाहते हैं तो | "
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर "
                    ]
                  }
                }
              }
            ],
            "help": [],
            "unknown": [],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर "
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I really need your mobile number to go further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे आगे बढ़ने के लिए सही  में आपका मोबाइल नंबर चाहिए | "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Just your mobile number and my human masters will be able to sort out all your issues."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "सिर्फ आपका मोबाइल नंबर चाहिए और मेरे ह्यूमन मास्टर्स आपकी सभी परेशानियों को दूर कर पाएँगे | "
                    ]
                  }
                }
              }
            ],
            "where": [],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would need your mobile number now to connect with my superiors."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपको अपने उच्च अधिकारियों (सीनियर्स ) के साथ जोड़ने के लिए मुझे आपके मोबाइल नंबर की ज़रूरत होगी।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f635977e117",
          "createdDate": "2019-01-22T08:43:35.210Z",
          "updatedDate": "2019-01-23T05:52:42.226Z",
          "deleted": false,
          "slug": "select-language",
          "defaultStep": false,
          "name": "select language",
          "description": "select language",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f2e3677e0c8",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please let me know the language you are comfortable in"
                ],
                "options": [
                  {
                    "title": "English",
                    "text": "english"
                  },
                  {
                    "title": "Hindi",
                    "text": "hindi"
                  }
                ]
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "othersInit"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f4d3677e12a",
          "createdDate": "2018-11-16T06:35:52.057Z",
          "updatedDate": "2018-11-16T07:17:27.119Z",
          "deleted": false,
          "slug": "type",
          "defaultStep": false,
          "name": "type",
          "description": "Type of product user wants to buy",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f343c77e0c9",
          "__v": 0,
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "buyOnineTypeValidator"
            }
          ],
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please select the type of insurance you would like to buy"
                ],
                "options": [
                  {
                    "title": "Health",
                    "text": "health"
                  },
                  {
                    "title": "Travel",
                    "text": "travel"
                  },
                  {
                    "title": "Car",
                    "text": "car"
                  },
                  {
                    "title": "Two Wheeler",
                    "text": "two wheeler"
                  },
                  {
                    "title": "Accident",
                    "text": "accident"
                  }
                ]
              }
            }
          ]
        },
        {
          "_id": "5c611fbce5378ff4d577e130",
          "createdDate": "2019-01-22T08:43:44.738Z",
          "updatedDate": "2019-01-25T12:15:47.720Z",
          "deleted": false,
          "slug": "email",
          "defaultStep": false,
          "name": "email",
          "description": "email",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f2e3677e0c8",
          "__v": 0,
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "emailValidator"
            }
          ],
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "emailQF"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! Waiting for your email Id."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! आपको रिन्यूअल नोटिस की कॉपी भेजने के लिए मुझे आपके ईमेल आईडी की ज़रुरत होगी | "
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Welcome!"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है !"
                    ]
                  }
                }
              },
              {
                "type": "quickReplies",
                "id": 1,
                "quickReplies": {
                  "title": [
                    ""
                  ],
                  "options": [
                    {
                      "title": "Option",
                      "text": ""
                    }
                  ]
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hmm.."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ह्म्म्म।"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would need your email id to send you any related information to your query."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपको रिन्यूअल नोटिस की सॉफ्ट कॉपी भेजने के लिए मुझे आपके ईमेल आईडी की ज़रुरत होगी |"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You ask what's email ? It's a fancy little thing by which people send and receive mails. Over the internet.! Fancy stuff if you ask me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      " क्या आप जानना चाहते हैं कि ईमेल क्या होता है? ये एक छोटी सी शानदार चीज़ है जिससे लोग सन्देश भेजते और पाते हैं; वो भी इंटरनेट पर | मेरी माने तो ये काफी आधुनिक है| "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "emailQF"
              }
            ],
            "how": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे नहीं लगता है कि मुझे ये समझ आया है| क्या आप दोबारा लिख सकते हैं ?"
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA  AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "😱😱"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "😱😱"
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.! I'll wait."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है।! मैं इंतजार करुँगी।"
                    ]
                  }
                }
              }
            ],
            "help": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Please contact our customer service executive to resolve your query."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "अपनी क्वेरी (सवालों) को हल करने के लिए कृपया हमारे ग्राहक सेवा कार्यकारी(कस्टमर सर्विस एग्जीक्यूटिव) से संपर्क करें।"
                    ]
                  }
                }
              }
            ],
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.. But I really need your email ID to proceed further. If you still don't have your id, please contact our customer service executive to resolve your query."
                ]
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ]
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I really need your email id to proceed further"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं आपके रिन्यूअल नोटिस की कॉपी और कैसे भेज सकती हूँ "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Uh-Noo. You're almost there. Just give your email id and I'll connect you with our agent  right away."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ओह| आपका काम लगभग हो गया है| बस अपना ईमेल आईडी दे दीजिए और मैं आपका रिन्यूअल नोटिस तुरंत भेज दूंगी | "
                    ]
                  }
                }
              }
            ],
            "where": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "जैसे ही आप मुझे अपना ईमेल आईडी देते हैं, मैं आपका  रिन्यूअल नोटिस भेज दूँगी ।"
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'll be connecting you as soon as you give me your email id."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "जैसे ही आप मुझे अपना ईमेल आईडी देते हैं, मैं आपका  रिन्यूअल नोटिस भेज दूँगी ।"
                    ]
                  }
                }
              }
            ],
            "ZX": []
          }
        },
        {
          "_id": "5c611fbce5378feaf077e13f",
          "createdDate": "2019-02-09T18:36:44.056Z",
          "updatedDate": "2019-02-09T20:14:17.872Z",
          "deleted": false,
          "slug": "change-title",
          "defaultStep": false,
          "name": "change title",
          "description": "change title",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please choose your title"
                ],
                "options": [
                  {
                    "title": "Mr",
                    "text": ""
                  },
                  {
                    "title": "Ms",
                    "text": ""
                  }
                ]
              }
            }
          ]
        },
        {
          "_id": "5c611fbce5378f90a377e13b",
          "createdDate": "2019-02-09T18:35:40.351Z",
          "updatedDate": "2019-02-09T20:32:18.379Z",
          "deleted": false,
          "slug": "change-pancard",
          "defaultStep": false,
          "name": "change pancard",
          "description": "change pancard",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please tell me your pan card number"
              ]
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nilPanValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f74d977e134",
          "createdDate": "2019-02-09T18:33:52.457Z",
          "updatedDate": "2019-02-09T18:39:46.148Z",
          "deleted": false,
          "slug": "cust-name",
          "defaultStep": false,
          "name": "cust name",
          "description": "cust name",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "custNameQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nameValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f560677e137",
          "createdDate": "2019-02-09T18:34:31.836Z",
          "updatedDate": "2019-02-09T19:09:39.758Z",
          "deleted": false,
          "slug": "change-email-id",
          "defaultStep": false,
          "name": "change email id",
          "description": "change email id",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please enter your new email id."
              ]
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nilEmailValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f285477e11f",
          "createdDate": "2018-11-29T07:32:37.309Z",
          "updatedDate": "2018-12-11T04:39:17.748Z",
          "deleted": false,
          "slug": "type",
          "defaultStep": false,
          "name": "type",
          "description": "type of enquiry",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f27ec77e0d1",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please choose the type to proceed."
                ],
                "options": [
                  {
                    "title": "Policy Brochures",
                    "text": "brochure"
                  },
                  {
                    "title": "Policy Wordings ",
                    "text": "wording"
                  },
                  {
                    "title": "Tie-ups & Locators",
                    "text": "locators"
                  }
                ]
              },
              "locale": {
                "hi": {
                  "type": "quickReplies",
                  "id": 0,
                  "quickReplies": {
                    "title": [
                      ""
                    ],
                    "options": [
                      {
                        "title": "Policy Brochures",
                        "text": "brochure"
                      },
                      {
                        "title": "Option",
                        "text": ""
                      }
                    ]
                  }
                }
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "gqTypeValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f690a77e12e",
          "createdDate": "2018-11-16T04:51:00.432Z",
          "updatedDate": "2019-01-25T12:06:09.072Z",
          "deleted": false,
          "slug": "mobile",
          "defaultStep": false,
          "name": "mobile",
          "description": "Ask users mobile number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f52f877e0cc",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileQf"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I'm still waiting for your mobile number."
                ]
              }
            ],
            "courtesy": [],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ]
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I want your mobile number so that we can get in contact with you if this conversation left unfinished"
                ]
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  " My masters know better. Just tell me your mobile number and I'll connect you with them."
                ]
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "mobileQuestionFunction"
              }
            ],
            "how": [],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ]
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Abusing doesn't help at all. Spread love. Spread peace."
                ]
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ]
              }
            ],
            "help": [],
            "unknown": [],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ]
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would really need your mobile number to proceed further."
                ]
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You're so close to buying insurance online. Just you're mobile number and we will be on our way.."
                ]
              }
            ],
            "where": [],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would need your mobile number now to connect with my superiors."
                ]
              }
            ],
            "ZX": []
          }
        },
        {
          "_id": "5c611fbce5378fa94f77e132",
          "createdDate": "2019-02-09T18:32:36.682Z",
          "updatedDate": "2019-02-12T08:24:24.970Z",
          "deleted": false,
          "slug": "mobile-number",
          "defaultStep": false,
          "name": "Mobile number",
          "description": "mobile number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 5,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileQf"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378fbed877e124",
          "createdDate": "2018-11-29T07:33:19.925Z",
          "updatedDate": "2018-12-03T08:49:11.025Z",
          "deleted": false,
          "slug": "policy-brochures",
          "defaultStep": false,
          "name": "policy brochures",
          "description": "policy brochures like travel products etc\n",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f27ec77e0d1",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please choose the category of Products"
                ],
                "options": [
                  {
                    "title": "Travel Products",
                    "text": "travel"
                  },
                  {
                    "title": "Accident and Health Products",
                    "text": "health"
                  }
                ]
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "policyBrouchureValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f826277e128",
          "createdDate": "2018-12-07T05:20:18.768Z",
          "updatedDate": "2018-12-19T14:57:07.442Z",
          "deleted": false,
          "slug": "secondary-email",
          "defaultStep": false,
          "name": "secondary email",
          "description": "secondary email",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f264777e0c6",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please enter your secondary email Id"
                ],
                "options": [
                  {
                    "title": "I don't have a secondary email Id",
                    "text": "noemailid"
                  }
                ]
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "secondaryEmailValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378fe48877e122",
          "createdDate": "2019-01-23T05:37:43.715Z",
          "updatedDate": "2019-01-25T12:14:34.185Z",
          "deleted": false,
          "slug": "policy-number",
          "defaultStep": false,
          "name": "policy number",
          "description": "policy number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f2e3677e0c8",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "othersPolicyNumberQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "othersPolicyValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hey, Could you please share your policy number.",
                  "Hello, Could you please share your policy number.",
                  "Hi there, Could you please share your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "कृपया क्या आप अपना पॉलिसी नंबर बता सकते हैं।",
                      "नमस्कार! क्या आप अपना पॉलिसी नंबर बता सकते हैं ।",
                      "नमस्ते, क्या आप अपना पॉलिसी नंबर बता सकते हैं| "
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You are welcome.",
                  "Its my pleasure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है।",
                      "ये मेरे लिए ख़ुशी की बात है | "
                    ]
                  }
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hmm. Could you please provide me your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "हम्म। क्या आप कृपया मुझे अपना पॉलिसी नंबर दे सकते हैं।"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "To serve you better, I need your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपकी पॉलिसी की सॉफ्ट कॉपी आपको देने के लिए मुझे आपके पॉलिसी नंबर की ज़रूरत होगी  "
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे ये ठीक से समझ नहीं आया है| क्या आप इसे दोबारा लिख सकते हैं| "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure, I need your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर, मुझे आपका पॉलिसी नंबर चाहिए | "
                    ]
                  }
                }
              }
            ],
            "how": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे नहीं लगता है कि मुझे ये समझ आया है| क्या आप दोबारा लिख सकते हैं | "
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sorry for the inconvenience, Could you please provide your policy number so that we can serve you better."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "परेशानी के लिए माफ़ी चाहूँगी, क्या आप कृपया अपना पॉलिसी नंबर दे सकते हैं ताकि हम आपको पॉलिसी की सॉफ्ट कॉपी दे सकें।"
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.",
                  "Take your own time."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर।",
                      "आप ज़रूरी समय ले सकते हैं |"
                    ]
                  }
                }
              }
            ],
            "help": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I will surely help you, but i need your policy number to proceed."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं आपकी मदद ज़रूर करुँगी, लेकिन आगे बढ़ने के लिए मुझे आपका पॉलिसी नंबर चाहिए | "
                    ]
                  }
                }
              }
            ],
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm sorry but I need your policy number to proceed. "
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "माफ़ कीजिए, लेकिन आगे बढ़ने के लिए मुझे आपका पॉलिसी नंबर चाहिए | "
                    ]
                  }
                }
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.",
                  "Could you please provide me your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है।",
                      "क्या आप कृपया मुझे अपना पॉलिसी नंबर दे सकते हैं।"
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sorry. I will not be able to proceed further with out your policy number. Could you please share your policy number."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "माफ़ कीजिए। मैं आपके पॉलिसी नंबर के बिना आगे नहीं बढ़ सकती हूँ। क्या आप कृपया अपना पॉलिसी नंबर बता सकते हैं।"
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Bye.",
                  "Thank you.",
                  "Nice talking to you.",
                  "See you later.",
                  "Hope to see you soon."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "अलविदा/बाय।",
                      "धन्यवाद।",
                      "आपसे बात करके अच्छा लगा।",
                      "फिर मिलेंगे ",
                      "आशा है, आप जल्दी ही हमें सेवा का मौका देंगे।"
                    ]
                  }
                }
              }
            ],
            "where": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You can find your policy number in your policy documents."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपको अपना पॉलिसी नंबर अपने पॉलिसी डॉक्युमेंट्स में मिल जाएगा|"
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "If possible now, or else i will wait for you."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "हो सके तो अभी नहीं तो मैं इंतज़ार कर सकती हूँ "
                    ]
                  }
                }
              }
            ],
            "ZX": []
          }
        },
        {
          "_id": "5c611fbce5378fbf0477e126",
          "createdDate": "2018-11-29T07:34:11.361Z",
          "updatedDate": "2018-12-04T05:36:55.004Z",
          "deleted": false,
          "slug": "brochure-travel",
          "defaultStep": false,
          "name": "brochure travel",
          "description": "brochure_travel",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f27ec77e0d1",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please choose a Travel Insurance Product"
                ],
                "options": [
                  {
                    "title": "Travel Guard ",
                    "text": "Travel Guard "
                  },
                  {
                    "title": "Student Guard Plus Policy",
                    "text": "Student Guard Plus Policy"
                  },
                  {
                    "title": "Domestic Travel Guard Policy",
                    "text": "Domestic Travel Guard Policy"
                  },
                  {
                    "title": "Asia Travel Guard Policy",
                    "text": "Asia Travel Guard Policy"
                  }
                ]
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "brochureTravelValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f811e77e12f",
          "createdDate": "2018-12-04T06:37:36.956Z",
          "updatedDate": "2018-12-04T06:42:19.902Z",
          "deleted": false,
          "slug": "mobile-number",
          "defaultStep": false,
          "name": "mobile-number",
          "description": "mobile number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f996377e0d2",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileQf"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f37f377e135",
          "createdDate": "2019-02-09T18:34:05.344Z",
          "updatedDate": "2019-02-09T18:46:27.696Z",
          "deleted": false,
          "slug": "email-id",
          "defaultStep": false,
          "name": "email id",
          "description": "email id",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "emailQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "emailValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f1eec77e116",
          "createdDate": "2018-12-04T06:46:20.847Z",
          "updatedDate": "2018-12-12T10:18:37.946Z",
          "deleted": false,
          "slug": "location",
          "defaultStep": false,
          "name": "location",
          "description": "Location",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f996377e0d2",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 1,
              "func": "takeLocation"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "tieUplocationValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f0c9577e118",
          "createdDate": "2018-11-29T07:33:58.086Z",
          "updatedDate": "2018-12-03T11:36:53.250Z",
          "deleted": false,
          "slug": "policy-wordings",
          "defaultStep": false,
          "name": "policy wordings",
          "description": "policy wordings like motor products\n\n",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f27ec77e0d1",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please choose the category of Products"
                ],
                "options": [
                  {
                    "title": "Motor Products",
                    "text": "motor"
                  },
                  {
                    "title": "Travel Products",
                    "text": "travel"
                  },
                  {
                    "title": "Accident and Health Products",
                    "text": "health"
                  },
                  {
                    "title": "Home Insurance Products",
                    "text": "home"
                  }
                ]
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "policyWordingValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378fa7a377e121",
          "createdDate": "2019-01-22T08:43:53.645Z",
          "updatedDate": "2019-01-25T12:15:35.276Z",
          "deleted": false,
          "slug": "mobile",
          "defaultStep": false,
          "name": "mobile",
          "description": "mobile",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f2e3677e0c8",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileQf"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "agentMobileValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I'm still waiting for your mobile number."
                ]
              }
            ],
            "courtesy": [],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ]
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I want your mobile number so that we can get in contact with you if this conversation left unfinished"
                ]
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  " My masters know better. Just tell me your mobile number and I'll connect you with them."
                ]
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "mobileQuestionFunction"
              }
            ],
            "how": [],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ]
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Abusing doesn't help at all. Spread love. Spread peace."
                ]
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ]
              }
            ],
            "help": [],
            "unknown": [],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ]
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would really need your mobile number to proceed further."
                ]
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You're so close to buying insurance online. Just you're mobile number and we will be on our way.."
                ]
              }
            ],
            "where": [],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would need your mobile number now to connect with my superiors."
                ]
              }
            ],
            "ZX": []
          }
        },
        {
          "_id": "5c611fbce5378f600777e123",
          "createdDate": "2018-11-29T07:31:42.790Z",
          "updatedDate": "2018-12-11T04:35:04.229Z",
          "deleted": false,
          "slug": "cust-name",
          "defaultStep": false,
          "name": "cust name",
          "description": "customer name\n",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f27ec77e0d1",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "custNameQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nameValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello again! I'm waiting for your name"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "फिर से नमस्कार! कृपया मुझे अपना नाम बताएँ| "
                    ]
                  }
                }
              }
            ],
            "courtesy": [],
            "okay": [],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I think it's a good start by knowing each other. I'm Tara and what's your name?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "चलिए, एक दूसरे को जानने से शुरुआत करते हैं । मैं तारा हूँ और आपका नाम क्या है?"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Name is a name. It can be any name. Commonly it is what people call you by."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नाम बस एक नाम है। यह कोई भी नाम हो सकता है। आमतौर यह वो होता है जिससे लोग आपको पुकारते हैं| "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "custNameQF"
              }
            ],
            "how": [],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA AIG की  डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I know you are impatient but could please mention your name, so that I can resolve your problem."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे पता है कि आपको जल्दी है लेकिन कृपया अपना नाम बताएँ, ताकि मैं आपकी समस्या  का हल निकाल सकूँ| "
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Ok! I'm waiting."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है ! मैं इंतज़ार कर रही हूँ।"
                    ]
                  }
                }
              }
            ],
            "help": [],
            "unknown": [],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर "
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "What's there in sharing a name. I really need your name to proceed further."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नाम बताने में क्या परेशानी है| आगे बढ़ने के लिए मुझे सही में आपके नाम की ज़रूरत होगी "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Oh. Really sad not to help you. Anyways, if you need anything else, I'll always be here."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ओह| आपको बेहतर सेवा न दे पाने का मुझे दुःख है। अगर आपको कुछ और मदद चाहिए तो मैं हमेशा तैयार हूँ।"
                    ]
                  }
                }
              }
            ],
            "where": [],
            "when": []
          }
        },
        {
          "_id": "5c611fbce5378f368977e139",
          "createdDate": "2019-02-09T18:35:06.793Z",
          "updatedDate": "2019-03-07T05:34:49.215Z",
          "deleted": false,
          "slug": "change-marital-status",
          "defaultStep": false,
          "name": "change marital status",
          "description": "change marital status",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 14,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please select your marital status"
                ],
                "options": [
                  {
                    "title": "Single",
                    "text": ""
                  },
                  {
                    "title": "Married",
                    "text": ""
                  },
                  {
                    "title": "Unknown",
                    "text": ""
                  },
                  {
                    "title": "Widowed",
                    "text": ""
                  },
                  {
                    "title": "Divorced",
                    "text": ""
                  }
                ]
              }
            }
          ]
        },
        {
          "_id": "5c611fbce5378f26f277e13c",
          "createdDate": "2019-02-09T18:35:54.361Z",
          "updatedDate": "2019-02-09T19:11:38.931Z",
          "deleted": false,
          "slug": "change-contact-number",
          "defaultStep": false,
          "name": "change contact number",
          "description": "change contact number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please tell me your new mobile number"
              ]
            }
          ]
        },
        {
          "_id": "5c611fbce5378f4e8877e13d",
          "createdDate": "2019-02-09T18:36:19.465Z",
          "updatedDate": "2019-02-09T20:32:57.238Z",
          "deleted": false,
          "slug": "change-aadhaar-number",
          "defaultStep": false,
          "name": "change aadhaar number",
          "description": "change aadhaar number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 0,
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nilaadhaarValidator"
            }
          ],
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please enter your Aadhaar card number"
              ]
            }
          ]
        },
        {
          "_id": "5c611fbce5378f3db177e133",
          "createdDate": "2019-02-09T18:33:12.619Z",
          "updatedDate": "2019-03-07T05:08:27.996Z",
          "deleted": false,
          "slug": "verify-otp",
          "defaultStep": false,
          "name": "verify otp",
          "description": "verify otp",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 1,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please enter the OTP received on your registered contact number"
                ],
                "options": [
                  {
                    "title": "Resend OTP",
                    "text": "resend otp again"
                  },
                  {
                    "title": "Change number",
                    "text": "change number"
                  }
                ]
              }
            }
          ]
        },
        {
          "_id": "5c611fbce5378f71f177e138",
          "createdDate": "2019-02-09T18:34:48.793Z",
          "updatedDate": "2019-02-09T19:10:04.647Z",
          "deleted": false,
          "slug": "change-alternate-email-id",
          "defaultStep": false,
          "name": "change alternate email id",
          "description": "change alternate email id",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please enter your new alternate email id"
              ]
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nilAltEmailValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f87dd77e13e",
          "createdDate": "2019-02-09T18:36:33.991Z",
          "updatedDate": "2019-02-09T20:33:27.447Z",
          "deleted": false,
          "slug": "change-vehicle-number",
          "defaultStep": false,
          "name": "change vehicle number",
          "description": "change vehicle number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please enter the new vehicle number"
              ]
            }
          ]
        },
        {
          "_id": "5c611fbce5378f230077e120",
          "createdDate": "2018-12-04T06:37:52.122Z",
          "updatedDate": "2018-12-04T06:42:40.756Z",
          "deleted": false,
          "slug": "email-id",
          "defaultStep": false,
          "name": "email-id",
          "description": "email id",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f996377e0d2",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "emailQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "emailValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f56e577e125",
          "createdDate": "2018-11-29T07:35:10.479Z",
          "updatedDate": "2018-12-03T18:07:00.914Z",
          "deleted": false,
          "slug": "wording-home",
          "defaultStep": false,
          "name": "wording home",
          "description": "wording_home",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f27ec77e0d1",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please choose a Home Insurance Product"
                ],
                "options": [
                  {
                    "title": "Group Credit secure Policy ",
                    "text": "group_credit"
                  },
                  {
                    "title": "Home Secure – SFSP",
                    "text": "home_secure_sfsp"
                  },
                  {
                    "title": "Home Gaurd Policy",
                    "text": "home_gaurd"
                  },
                  {
                    "title": "Home Secure (Householders) InstaChoice Policy ",
                    "text": "instachoice"
                  },
                  {
                    "title": "Home Secure (Householders) Policy",
                    "text": "home_secure"
                  }
                ]
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "wordingHomeValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378fa7c177e127",
          "createdDate": "2018-12-04T06:37:10.392Z",
          "updatedDate": "2018-12-04T06:41:49.983Z",
          "deleted": false,
          "slug": "cust-name",
          "defaultStep": false,
          "name": "cust-name",
          "description": "customer name",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f996377e0d2",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "custNameQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nameValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378fa96f77e129",
          "createdDate": "2018-11-16T04:51:41.685Z",
          "updatedDate": "2019-01-25T12:11:55.169Z",
          "deleted": false,
          "slug": "email",
          "defaultStep": false,
          "name": "email",
          "description": "ask users email id",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f52f877e0cc",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "emailQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "emailValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! Waiting for your email Id."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! आपको रिन्यूअल नोटिस की कॉपी भेजने के लिए मुझे आपके ईमेल आईडी की ज़रुरत होगी | "
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Welcome!"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है !"
                    ]
                  }
                }
              },
              {
                "type": "quickReplies",
                "id": 1,
                "quickReplies": {
                  "title": [
                    ""
                  ],
                  "options": [
                    {
                      "title": "Option",
                      "text": ""
                    }
                  ]
                }
              }
            ],
            "okay": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hmm.."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ह्म्म्म।"
                    ]
                  }
                }
              }
            ],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I would need your email id to send you any related information to your query."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपको रिन्यूअल नोटिस की सॉफ्ट कॉपी भेजने के लिए मुझे आपके ईमेल आईडी की ज़रुरत होगी |"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You ask what's email ? It's a fancy little thing by which people send and receive mails. Over the internet.! Fancy stuff if you ask me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      " क्या आप जानना चाहते हैं कि ईमेल क्या होता है? ये एक छोटी सी शानदार चीज़ है जिससे लोग सन्देश भेजते और पाते हैं; वो भी इंटरनेट पर | मेरी माने तो ये काफी आधुनिक है| "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "emailQF"
              }
            ],
            "how": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे नहीं लगता है कि मुझे ये समझ आया है| क्या आप दोबारा लिख सकते हैं ?"
                    ]
                  }
                }
              }
            ],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मेरा नाम तारा है। मैं TATA  AIG की डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "😱😱"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "😱😱"
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.! I'll wait."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है।! मैं इंतजार करुँगी।"
                    ]
                  }
                }
              }
            ],
            "help": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Please contact our customer service executive to resolve your query."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "अपनी क्वेरी (सवालों) को हल करने के लिए कृपया हमारे ग्राहक सेवा कार्यकारी(कस्टमर सर्विस एग्जीक्यूटिव) से संपर्क करें।"
                    ]
                  }
                }
              }
            ],
            "unknown": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.. But I really need your email ID to proceed further. If you still don't have your id, please contact our customer service executive to resolve your query."
                ]
              }
            ],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure.."
                ]
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I really need your email id to proceed further"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं आपके रिन्यूअल नोटिस की कॉपी और कैसे भेज सकती हूँ "
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Uh-Noo. You're almost there. Just give your email id and I'll connect you with our agent  right away."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ओह| आपका काम लगभग हो गया है| बस अपना ईमेल आईडी दे दीजिए और मैं आपका रिन्यूअल नोटिस तुरंत भेज दूंगी | "
                    ]
                  }
                }
              }
            ],
            "where": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'm not sure I understood what you meant. Can you please rephrase?"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "जैसे ही आप मुझे अपना ईमेल आईडी देते हैं, मैं आपका  रिन्यूअल नोटिस भेज दूँगी ।"
                    ]
                  }
                }
              }
            ],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'll be connecting you as soon as you give me your email id."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "जैसे ही आप मुझे अपना ईमेल आईडी देते हैं, मैं आपका  रिन्यूअल नोटिस भेज दूँगी ।"
                    ]
                  }
                }
              }
            ],
            "ZX": []
          }
        },
        {
          "_id": "5c611fbce5378f75f477e13a",
          "createdDate": "2019-02-09T18:35:26.071Z",
          "updatedDate": "2019-02-09T19:36:29.023Z",
          "deleted": false,
          "slug": "change-occupation",
          "defaultStep": false,
          "name": "change occupation",
          "description": "change occupation",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please let me know what you do for living"
              ]
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "occupationValidator"
            }
          ],
          "autoComplete": "occupationAutoComplete"
        },
        {
          "_id": "5c611fbce5378f2f8977e12d",
          "createdDate": "2018-11-29T07:32:06.905Z",
          "updatedDate": "2018-12-11T04:38:21.611Z",
          "deleted": false,
          "slug": "email-id",
          "defaultStep": false,
          "name": "email id",
          "description": "email id",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f27ec77e0d1",
          "__v": 0,
          "prompts": [
            {
              "type": "func",
              "id": 0,
              "func": "emailQF"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "emailValidator"
            }
          ],
          "responses": {
            "greeting": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Hello! I would need your email id to make your claim"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "नमस्कार! कृपया मुझे अपना ईमेल आईडी दें"
                    ]
                  }
                }
              }
            ],
            "courtesy": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Welcome!"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "आपका स्वागत है!"
                    ]
                  }
                }
              }
            ],
            "okay": [],
            "why": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I  would need your email id to make your claim"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मुझे क्लेम करने के लिए आपके ईमेल आईडी की ज़रूरत होगी।"
                    ]
                  }
                }
              }
            ],
            "what": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "You ask what's email ? It's a fancy little thing by which people send and receive mails. Over the internet.! Fancy stuff if you ask me."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      " क्या आप जानना चाहते हैं कि ईमेल क्या होता है? ये एक छोटी सी शानदार चीज़ है जिससे लोग सन्देश भेजते और पाते हैं; वो भी इंटरनेट पर | मेरी माने तो ये काफी आधुनिक है| "
                    ]
                  }
                }
              }
            ],
            "repeat": [
              {
                "type": "func",
                "id": 0,
                "func": "emailQuestionFunction"
              }
            ],
            "how": [],
            "about": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "My name is Tara. I am TATA AIG's digital assistant."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "मैं तारा हूँ। मैं TATA AIG की  डिजिटल सहायक हूँ।"
                    ]
                  }
                }
              }
            ],
            "abuse": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "😱😱"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "😱😱"
                    ]
                  }
                }
              }
            ],
            "wait": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Okay.! I'll wait."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ठीक है।! मैं इंतजार करुँगी।"
                    ]
                  }
                }
              }
            ],
            "help": [],
            "unknown": [],
            "yes": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Sure"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ज़रूर "
                    ]
                  }
                }
              }
            ],
            "no": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I really need your email to make your claim"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "क्लेम बनाने के लिए मुझे वास्तव में आपके ईमेल आईडी की ज़रूरत होगी।"
                    ]
                  }
                }
              }
            ],
            "bye": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "Uh-Noo. You're almost there. Just give your email id and I'll make your claim right away."
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "ओह! आपका काम लगभग हो गया है| बस अपना ईमेल आईडी दें और मैं आपका क्लेम अभी कर  देती हूँ| "
                    ]
                  }
                }
              }
            ],
            "where": [],
            "when": [
              {
                "type": "text",
                "id": 0,
                "messages": [
                  "I'll be making your claim as soon as you tell me your mail id"
                ],
                "locale": {
                  "hi": {
                    "type": "text",
                    "id": 0,
                    "messages": [
                      "जैसे ही आप मुझे अपना मेल आईडी देते हैं , मैं आपका क्लेम कर दूंगी ।"
                    ]
                  }
                }
              }
            ]
          }
        },
        {
          "_id": "5c611fbce5378f420077e11b",
          "createdDate": "2018-11-29T07:35:00.083Z",
          "updatedDate": "2018-12-03T11:29:38.370Z",
          "deleted": false,
          "slug": "wording-health",
          "defaultStep": false,
          "name": "wording health",
          "description": "wording_health",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f27ec77e0d1",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please choose a Health and Accident Insurance Product"
                ],
                "options": [
                  {
                    "title": "Maharaksha - Personal Injury Plan",
                    "text": "maharaksha"
                  },
                  {
                    "title": "Individual Accident & Sickness Policy",
                    "text": "individual"
                  },
                  {
                    "title": "Hospital Cash Policy",
                    "text": "hospital_cash"
                  },
                  {
                    "title": "Hospital Care Policy",
                    "text": "hospital_care"
                  },
                  {
                    "title": "Complete Care Policy",
                    "text": "complete_care"
                  },
                  {
                    "title": "More",
                    "text": "more"
                  }
                ]
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "wordingHealthValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f672677e11d",
          "createdDate": "2018-11-29T07:34:36.653Z",
          "updatedDate": "2018-12-03T09:07:43.969Z",
          "deleted": false,
          "slug": "wording-motor",
          "defaultStep": false,
          "name": "wording motor",
          "description": "wording_motor",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378f27ec77e0d1",
          "__v": 0,
          "prompts": [
            {
              "type": "quickReplies",
              "id": 0,
              "quickReplies": {
                "title": [
                  "Please choose a Motor Insurance Product"
                ],
                "options": [
                  {
                    "title": "Private Car",
                    "text": "Private Car"
                  },
                  {
                    "title": "Two Wheeler",
                    "text": "Two Wheeler"
                  },
                  {
                    "title": "Commercial Vehicle",
                    "text": "Commercial Vehicle"
                  }
                ]
              }
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "wordingMotorValidator"
            }
          ]
        },
        {
          "_id": "5c611fbce5378f589f77e131",
          "createdDate": "2019-02-09T05:53:05.356Z",
          "updatedDate": "2019-02-10T06:49:50.483Z",
          "deleted": false,
          "slug": "policy-number",
          "defaultStep": false,
          "name": "policy number",
          "description": "policy number",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 0,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "It's seems you like to make some change's to your policy, surely I can help you with that."
              ]
            },
            {
              "type": "func",
              "id": 1,
              "func": "nilPolicyQf"
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nilPolicyValidator"
            }
          ]
        },
        {
          "_id": "5c65044934b4410e1026b5af",
          "createdDate": "2019-02-14T06:01:45.280Z",
          "updatedDate": "2019-02-14T08:42:23.629Z",
          "deleted": false,
          "slug": "change-pincode",
          "defaultStep": false,
          "name": "change pincode",
          "description": "change pincode",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 38,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please enter the new  pin code."
              ]
            }
          ],
          "autoComplete": "pincodeAutoComplete",
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nilPincodeValidator"
            }
          ]
        },
        {
          "_id": "5c65047934b441eafa26b5b0",
          "createdDate": "2019-02-14T06:02:33.810Z",
          "updatedDate": "2019-02-14T09:24:04.837Z",
          "deleted": false,
          "slug": "change-address",
          "defaultStep": false,
          "name": "change address",
          "description": "change address",
          "botId": "x1542952684229",
          "journeyId": "5c611fbce5378fb2ea77e0d4",
          "__v": 37,
          "prompts": [
            {
              "type": "text",
              "id": 0,
              "messages": [
                "Please enter your complete address"
              ]
            }
          ],
          "validators": [
            {
              "type": "func",
              "id": 0,
              "func": "nilAddressValidator"
            }
          ]
        }
      ]

functionsObj = [
        {
          "_id": "5c611fbc521f1e0011c7abac",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const record = {\n        \"request\" : JSON.stringify(args.request),\n        \"response\" : JSON.stringify(args.response),\n        \"error\" : JSON.stringify(args.error),\n        \"type\":args.type,\n        \"elapsed_time\":args.elapsedTime,\n        \"ticket_number\":args.ticketNumber?args.ticketNumber:\"\",\n        \"steps\":args.steps ? JSON.stringify(args.steps) : \"\",\n        \"xml_request\" : args.xmlrequest ? JSON.stringify(args.xmlrequest) : \"\"\n    }\n    app.dataStore.insert({\n        table:args.tableName,\n        record:record\n    })\n    return resolve();\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-25T08:47:05.843Z",
          "email": "parvez@yellowmessenger.com",
          "name": "apiResponseDatabase",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abad",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    try {\n        app.memory.get('userDetails').then(user => {\n            user = JSON.parse(user);\n            if (args.field === 'username') {\n                app.profile.username = args.value;\n                app.updateProfile();\n            }\n            user[args.field] = args.value;\n            app.memory.set('userDetails', user);\n            return resolve();\n        }).catch(err => {\n            const userDetails = {\n                mobile: {\n                    mobile1: \"\",\n                    mobile2: \"\"\n                }\n            };\n            if (args.field === 'username') {\n                app.profile.username = args.value;\n                app.updateProfile();\n            }\n            userDetails[args.field] = args.value;\n            app.memory.set('userDetails', userDetails);\n            return resolve();\n        });\n    } catch (err) {\n        app.log(err, \"ERROR in updateCustomerInformation\")\n        app.sendTextMessage(app.renderMessage('calim-error', {}, \"\"))\n        app.triggerIntent('anything-else', {});\n        return;\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-30T06:13:39.437Z",
          "email": "tagic12@tagic.com",
          "name": "updateCustomerInformation",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abae",
          "code": "const askName = () => {\n    return app.sendTextMessage(app.renderMessage('phone-number',{},'Please enter your 10 digit mobile number'));\n}\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    app.memory.get('userDetails').then(user => {\n        user = JSON.parse(user);\n        if (user.agentMobile) {\n            app.sendQuickReplies({\n                title: app.renderMessage('phone-number',{},\"Please enter your 10 digit mobile number\"),\n                options: [{\n                    title: user.agentMobile,\n                    text: user.agentMobile\n                }]\n            });\n            return resolve();\n        } else {\n            askName()\n            return resolve();\n        }\n    }).catch(err => {\n        askName()\n        return resolve();\n    })\n\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.125Z",
          "email": "parvez@yellowmessenger.com",
          "name": "agentMobileQf",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abaf",
          "code": "const askName = () => {\n    return app.sendTextMessage(app.renderMessage('email',{},'Please enter your registered email id'));\n}\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    app.memory.get('userDetails').then(user => {\n        user = JSON.parse(user);\n        if (user.email) {\n            app.sendQuickReplies({\n                title: app.renderMessage('email',{},\"Please enter your registered email id\"),\n                options: [{\n                    title: user.email,\n                    text: user.email\n                }]\n            });\n            return resolve();\n        } else {\n            askName()\n            return resolve();\n        }\n    }).catch(err => {\n        askName()\n        return resolve();\n    })\n\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.124Z",
          "email": "parvez@yellowmessenger.com",
          "name": "emailQF",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abb0",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    if (app.prediction.global_model.intent === 'yes' && app.prediction.global_model.confidence > 0.85) {\n        app.setContextParam('doc_type', 'Renewal Policy Document$').then(() => {\n            app.pushData({ doc_type: 'Renewal Policy Document$' }, app.context.intent);\n            return resolve();\n        })\n    } else if (app.prediction.global_model.intent === 'no' && app.prediction.global_model.confidence > 0.85) {\n        app.setContextParam('doc_type', 'New Business$').then(() => {\n            app.pushData({ doc_type: 'New Business$' }, app.context.intent);\n            return resolve();\n        })\n    } else {\n        app.sendTextMessage(app.renderMessage('doc-type', {}, 'Please choose from the below options')).then(() => {\n            app.sendQuickReplies({\n                title: app.renderMessage('doc-type-quick', {}, 'Have you ever renewed the policy'),\n                options: [\n                    {\n                        title: 'Yes',\n                        text: 'yes'\n                    },\n                    {\n                        title: 'No',\n                        text: 'no'\n                    }\n                ]\n            })\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-28T11:30:14.223Z",
          "email": "parvez@yellowmessenger.com",
          "name": "docTypeValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abb1",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const language = app.context.steps['select-language'].toLowerCase();\n    app.log(app.context.steps)\n    if (language === 'hindi' || /^.*hindi.*$/ig.test(app.data.message)) {\n        app.memory.set('selectedLanguage', 'hi');\n        app.clearContext();\n        app.data.message = 'services'\n        app.botOptions.targetLanguage = 'hi';\n        app.start(app.botOptions);\n    } else {\n        app.memory.set('selectedLanguage', 'en');\n        app.clearContext();\n        app.data.message = 'services'\n        app.start(app.botOptions)\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.126Z",
          "email": "parvez@yellowmessenger.com",
          "name": "changeLanguageValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abb2",
          "code": "return new Promise(function(resolve){\n  if(app.term){\n    app.memory.get(\"state_id\").then(state_id => {\n      app.log(state_id, \"STATE ID\");\n      app.dataStore.search({\n        table: \"districts\",\n        body: {\n          \"query\": {\n            \"bool\": {\n              \"must\":\n                {\"regexp\": { \"District_Name\": app.term.toLowerCase() + \".*\" }}\n              ,\n              \"filter\":\n                {\n                  \"match\": {\"District_State_FK\": state_id},\n                }\n            }\n          }\n        }\n      }).then((result) => {\n        return resolve(app._.map(result.hits.hits, function (hit) {\n          return [hit._source.District_Name, hit._source.District_Name + \"$\" + hit._source.District_ID_PK];\n        }))\n\n      },(e)=>{\n        app.log(e,\"error\");\n      })\n\n    })\n\n  }else{  resolve([]) }\n})",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-05T12:27:06.232Z",
          "email": "kishore@yellowmessenger.com",
          "name": "districtAutoComplete",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abb3",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    if (/^[1-9][0-9]{5}$/.test(app.data.message)) {\n        app.setContextParam('pincode', app.data.message).then(() => {\n            app.pushData({ Pincode: app.data.message }, app.context.intent);\n            return resolve();\n        })\n\n    } else {\n        return resolve({\n            success: false,\n            question: app.renderMessage('pincode-validator', {}, '')\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.125Z",
          "email": "parvez@yellowmessenger.com",
          "name": "pincodeValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abb4",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.validate(app.data.message).then((result) => {\n        if (!result) {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"driver-name\", {}, \"Please tell me your name\")\n            })\n        } else {\n            app.setContextParam('driver-name', result);\n            let data = { driver_name: result, transaction: \"Failed\" }\n            app.pushData(data, app.context.intent);\n            app.executeFunction('updateCustomerInformation', args = { field: \"driverName\", value: result });\n            return resolve();\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.127Z",
          "email": "parvez@yellowmessenger.com",
          "name": "driverNameValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abb5",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.validate(app.data.message).then((result) => {\n        if (!result) {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"phone-validator\", {}, \"Please enter a valid 10 digit mobile number\")\n            })\n        } else if (/^[6,7,8,9]\\d{9}$/ig.test(result)) {\n            result = result.toLowerCase();\n            app.setContextParam('agent-mobile', result);\n            let dataToPUsh ={ insured_mobile: result }\n            app.pushData(dataToPUsh, app.context.intent)\n            app.executeFunction('updateCustomerInformation', args = { field: \"insuredMobile\", value: result });\n            return resolve();\n        } else {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"phone-validator\", {}, \"Please enter a valid 10 digit mobile number\")\n            })\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.128Z",
          "email": "parvez@yellowmessenger.com",
          "name": "claimInsuredMobileValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abb6",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    if (app.data.message === '2' || app.data.message === '4') {\n        app.setStep('motorType', app.data.message);\n        return resolve();\n    }else if(app.data.message === 'c2'){\n        app.setStep('motor-type', '2').then(()=>{\n            app.setStep('motorType', \"Commercial\");\n                return resolve();\n\n        })\n    } else {\n        app.sendQuickReplies({\n            title: app.renderMessage('motor-type', {}, ''),\n            options: [\n                {\n                    title: \"Two Wheeler\",\n                    text: '2'\n                },\n                {\n                    title: \"Four Wheeler\",\n                    text: '4'\n                },\n                {\n                    title:\"Comercial Vehicle\",\n                    text:'c2'\n                }\n            ]\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-17T08:58:38.390Z",
          "email": "parvez@yellowmessenger.com",
          "name": "motorTypeValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abb7",
          "code": "\nconst skipIntents = ['log-payment-link', 'customer-care', 'change-language', 'others', 'services', 'anything-else']\n\nconst questionMapping = {\n    'policy-document': 'Policy soft copy',\n    'renewal-policy': 'Renewal notice document',\n    'preinspection-request': 'Pre-inspection request',\n    'preinspection-status': 'Pre-inspection status',\n    'renewal-request-payment': 'Renew policy',\n    'claim-intimation': 'Intimate claim',\n    'buy-online': 'Buy a new insurance policy',\n    'others': 'Talk to agent'\n}\n\nreturn new Promise(resolve => {\n    app.ai.predict(app.data.message.toLowerCase()).then((prediction) => {\n        if (prediction && prediction.intents) {\n            let intents = [];\n            app._.mapKeys(prediction.intents, function (value, intent) {\n                if (skipIntents.indexOf(intent) === -1) {\n                    intents.push(intent);\n                }\n            })\n            app.getMultipleJourneysBySlug(intents).then((result) => {\n                let options = [];\n                app._.forEach(result, (journey) => {\n                    options.push({\n                        title: journey.description,\n                        text: journey.description\n                    })\n                });\n                options.push(\n                    {\n                        title: 'Contact support',\n                        text: 'Contact support'\n                    },\n                    {\n                        title: 'Services',\n                        text: 'services'\n                    })\n                if (options && options.length > 2) {\n                    app.sendQuickReplies({\n                        title: app.renderMessage('unidentified', {}, ''),\n                        options: options\n                    }).then(() => {\n                        return resolve();\n                    })\n                } else {\n                    app.sendQuickReplies({\n                        title: 'Would you like me to connect you with our customer care',\n                        options: options\n                    }).then(() => {\n                        return resolve();\n                    });\n                }\n            })\n        }\n    });\n});\n\n",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-05T05:06:17.007Z",
          "email": "parvez@yellowmessenger.com",
          "name": "unknownMessages",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abb8",
          "code": "return new Promise(function (resolve) {\n    app.log('lsjdfjaslkjflkjsadlfjlkasjdflj')\n    app.memory.get('districtName').then((dist) => {\n        if (app.term) {\n            console.log(dist, \"DISTRICT ID\");\n            app.dataStore.search({\n                table: \"settling_office_mapping_details\",\n                body: {\n                    \"query\": {\n                        \"bool\": {\n                            \"must\":\n                            { \"regexp\": { \"city\": app.term.toLowerCase() + \".*\" } }\n                            ,\n                            \"filter\":\n                            {\n                                \"match\": { \"district\": dist },\n                            }\n                        }\n                    }\n                }\n            }).then((result) => {\n                resolve(app._.map(result.hits.hits, function (hit) {\n                    return [hit._source.city, hit._source.city + \"$\" + hit._source.settling_office + \"$\" + hit._source.settling_code + \"$\" + hit._source.pincode];\n                }))\n\n            }, (e) => {\n                app.log(e, \"error\");\n            })\n        } else { resolve([]) }\n    }).catch(err => {\n        app.log(err, \"errrorr\");\n        return resolve([]);\n    })\n})",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-09T20:18:32.020Z",
          "email": "parvez@yellowmessenger.com",
          "name": "claimCityAutoComplete",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abb9",
          "code": "const errorMessage = (data, requestBody, responseBody, error, elapsedTime) => {\n    app.pushData({ transaction: \"Failed\" }, app.context.intent);\n    app.executeFunction('crmApi', args = { data: data, status: 'Open', intentName: \"renewal-request-payment\" });\n    app.executeFunction('apiResponseDatabase', args = { request: requestBody, response: responseBody, error: error, tableName: \"renewal_request_api_database\", \"type\": \"Renewal Request\", \"elapsedTime\": elapsedTime })\n    return app.sendTextMessage(app.renderMessage('renewal-request-error', {}, \"There was some error while processing your request. Pelase try again.\")).then(() => {\n        app.clearContext();\n        app.memory.delete('renewal_request_leads_id');\n        app.data.message = 'help';\n        return app.start();\n    })\n};\n\nconst responseError = (data, requestBody, responseBody, error, elapsedTime, message, transaction) => {\n    app.pushData({ transaction: transaction }, app.context.intent);\n    app.executeFunction('crmApi', args = { data: data, status: 'Closed', intentName: \"renewal-request-payment\" });\n    app.executeFunction('apiResponseDatabase', args = { request: requestBody, response: responseBody, error: error, tableName: \"renewal_request_api_database\", \"type\": \"Renewal Request\", \"elapsedTime\": elapsedTime })\n    if (!message) {\n        app.memory.delete('renewal_request_leads_id');\n        app.triggerIntent('anything-else', {});\n        return;\n    }\n    return app.sendTextMessage(app.renderMessage(message, {}, \"There was some error while processing your preinspection request. Pelase try again.\")).then(() => {\n        app.clearContext();\n        app.memory.delete('renewal_request_leads_id');\n        app.data.message = 'help';\n        return app.start();\n    })\n}\nconst responseSuccess = (data, requestBody, responseBody, error, elapsedTime, cards, transaction) => {\n    app.pushData({ transaction: transaction, paynow_method: cards }, app.context.intent);\n    app.executeFunction('crmApi', args = { data: data, status: 'Closed', intentName: \"renewal-request-payment\" });\n    app.memory.delete('renewal_request_leads_id');\n    app.executeFunction('apiResponseDatabase', args = { request: requestBody, response: responseBody, error: error, tableName: \"renewal_request_api_database\", \"type\": \"Renewal Request\", \"elapsedTime\": elapsedTime })\n    return;\n}\n\nreturn new Promise(resolve => {\n    const userData = {\n        username: app.context.steps['cust-name'],\n        mobileNo: app.context.steps['mobile-number'],\n        email: app.context.steps['email-id'],\n        policyNo: app.context.steps['policy-number']\n    };\n    const reqBody = `<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:ren=\"http://stub.unotechsoft.com/wsdl/RenewalStatus/\">\n                        <soapenv:Header/>\n                        <soapenv:Body>\n                            <ren:getRenewalStatusRequest>\n                    <!--Optional:-->\n                    <ren:getRenewalStatusRequest>\n                    <!--Optional:-->\n                    <Source>TATA-AIG</Source>\n                    <!--Optional:-->\n                    <Medium>CHATBOT</Medium>\n                    <!--Optional:-->\n                    <Campaign>CHATBOT</Campaign>\n                    <!--Optional:-->\n                    <AuthenticationToken></AuthenticationToken>\n                    <!--Optional:-->\n                    <policynumber>${app.context.steps['policy-number']}</policynumber>\n                    </ren:getRenewalStatusRequest>\n                    </ren:getRenewalStatusRequest>\n                    </soapenv:Body>\n                    </soapenv:Envelope>`;\n    app.requestOptions.url = app.renewalRequestUrl;\n    app.requestOptions.body = reqBody;\n    const startTime = new Date();\n    app.log(app.requestOptions, \"Renewal request options\")\n    app.request.request(app.requestOptions, function (err, res, body) {\n        app.elapsedTime(startTime).then(time => {\n            if (err || res.statusCode !== 200) {\n                errorMessage(userData, app.requestOptions, body, err, time);\n                return resolve();\n            } else {\n                let result = JSON.parse(app.xmlToJSON.toJson(body));\n                try {\n                    if (result[\"soap:Envelope\"] &&\n                        result[\"soap:Envelope\"][\"soap:Body\"] &&\n                        result[\"soap:Envelope\"][\"soap:Body\"][\"ns3:getRenewalStatusResponse\"] &&\n                        result[\"soap:Envelope\"][\"soap:Body\"][\"ns3:getRenewalStatusResponse\"][\"ns2:GetRenewalStatusResult\"]) {\n\n                        const details = result[\"soap:Envelope\"][\"soap:Body\"][\"ns3:getRenewalStatusResponse\"][\"ns2:GetRenewalStatusResult\"];\n                        app.log(details, \"GOT DETAILS FOR RENEWAL PAYMENT\");\n                        if (details.renewalStatus && details.renewalStatus === \"DECLINED\") {\n                            responseError(userData, app.requestOptions, result, err, time, \"renewal-request-declined\", \"Declined\");\n                        } else if (details.renewalStatus == \"PolicyNumber Not Found\" || details.renewalStatus === \"Policy not found\") {\n                            responseError(userData, app.requestOptions, result, err, time, \"renewal-request-policy-number-not-found\", \"Policy Number not found\");\n                            return resolve();\n                        } else if (details.renewalStatus === \"Policy Not due for renewal\") {\n                            responseError(userData, app.requestOptions, result, err, time, \"renewal-request-not-due\", \"Policy Number not Due for Renewal\");\n                            return resolve();\n                        } else {\n                            app.executeFunction('getPaymentLink', args = { details: details, policyNo: app.context.steps['policy-number'], userDetails: userData }).then(cards => {\n                                if (!cards) {\n                                    responseError(userData, app.requestOptions, result, err, time, cards, \"Success\")\n                                    return resolve();\n                                } else {\n                                    if (app.source === 'facebook') {\n                                        app.sendQuickReplies(cards).then(() => {\n                                            responseSuccess(userData, app.requestOptions, result, err, time, JSON.stringify(cards), \"Success\")\n                                            return resolve();\n                                        })\n                                    } else {\n                                        app.sendCards(cards).then(() => {\n                                            responseSuccess(userData, app.requestOptions, result, err, time, JSON.stringify(cards), \"Success\")\n                                            return resolve();\n                                        })\n                                    }\n                                }\n                            })\n                        }\n\n                    } else {\n                        errorMessage(userData, app.requestOptions, body, err, time);\n                        return resolve();\n                    }\n                } catch (err) {\n                    app.log(err, \"ERROR in RENEWAL STATUS\")\n                    errorMessage(userData, app.requestOptions, body, err, time);\n                    return resolve();\n                }\n            }\n        })\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-31T17:46:55.492Z",
          "email": "parvez@yellowmessenger.com",
          "name": "renewalRequestAction",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abba",
          "code": "function redact(mobile) {\n    return mobile.slice(0, 3) + \"****\" + mobile.slice(7, 10)\n}\nreturn new Promise(resolve => {\n    // Your logic goes here\n    app.setContextParam('verify-otp', undefined);\n    app.memory.get('userDetails').then((user) => {\n        user = JSON.parse(user);\n        if (app.data.message === user.mobile.mobile1 || app.data.message === user.mobile.mobile2) {\n            //Setting OTP rensend Count to profile\n            app.profile.resendOtpCount = 1;\n            app.updateProfile();\n            if (app.UAT_ENV) {\n                app.sendOtp(app.testMobile).then(() => {\n                    app.sendTextMessage(app.renderMessage('send-otp', { mobile: redact(app.testMobile) }, 'Please wait while I send an OTP to ' + redact(app.testMobile))).then(() => {\n                        app.memory.get('otp').then((otp) => {\n                            app.sendTextMessage(otp);\n                            app.setContextParam('mobile',app.testMobile);\n                            app.setContextParam('mobile-number', redact(app.testMobile)).then(() => {\n                                app.profile.selectedNumber = app.testMobile;\n                                app.updateProfile();\n                                app.pushData({ mobile_number: app.testMobile }, app.context.intent)\n                                app.log(otp, \"OTP\");\n                                return resolve();\n                            })\n                        })\n                    })\n                })\n            } else {\n                app.sendOtp(app.data.message).then(() => {\n                    app.sendTextMessage(app.renderMessage('send-otp', { mobile: redact(app.testMobile) }, 'Please wait while I send an OTP to ' + redact(app.testMobile))).then(() => {\n                        app.memory.get('otp').then((otp) => {\n                            app.setContextParam('mobile',app.data.message);\n                            app.setContextParam('mobile-number', redact(app.data.message)).then(() => {\n                                app.pushData({ mobile_number: app.data.message }, app.context.intent)\n                                app.profile.selectedNumber = app.data.message;\n                                app.updateProfile();\n                                app.log(otp, \"OTP\");\n                                return resolve();\n                            })\n                        })\n                    })\n                });\n            }\n        } else {\n            let opt = [];\n            if (user.mobile.mobile1) {\n                opt.push({\n                    title: redact(user.mobile.mobile1),\n                    text: user.mobile.mobile1\n                })\n            }\n            if (user.mobile.mobile2) {\n                opt.push({\n                    title: redact(user.mobile.mobile2),\n                    text: user.mobile.mobile2\n                })\n            }\n            app.sendQuickReplies({\n                title: app.renderMessage(\"select-mobile\", {}, \"Please select a mobile number for OTP verification\"),\n                options: opt\n            }, { hideInput: true })\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-25T09:10:26.194Z",
          "email": "parvez@yellowmessenger.com",
          "name": "mobileValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abbb",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const result = app.data.message.split('$');\n    if (result.length < 2 || result.length > 2) {\n        return resolve({\n            success: false,\n            question: app.renderMessage('state', {}, \"\")\n        })\n    } else {\n        app.setContextParam('state-id', result[1]).then(() => {\n            app.memory.set('state_id', result[1]);\n            app.setContextParam('state-name', result[0]).then(() => {\n                if (app.context.intent === 'claim-intimation') {\n                    app.pushData({ loss_state: result[0] }, app.context.intent);\n                    return resolve();\n                } else {\n                    app.pushData({ StateValue: result[0] }, app.context.intent);\n                    return resolve();\n                }\n            })\n        })\n    }\n});\n",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.130Z",
          "email": "parvez@yellowmessenger.com",
          "name": "stateValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abbc",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.dataStore.search({\n        table: args.table,\n        body: args.es_query\n    }).then((result) => {\n        if (result && result.hits.hits && result.hits.hits.length > 0) {\n            return resolve(result.hits.hits[0]._source);\n        } else {\n            return resolve(false);\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-09T19:38:06.618Z",
          "email": "parvez@yellowmessenger.com",
          "name": "searchQuery",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abbd",
          "code": "return new Promise((resolve, reject) => {\n    let value = app.data.message.toUpperCase();\n    value = value.trim();\n    let splits = value.split(\" \");\n    if (splits.length != 3) {\n        return resolve({\n            success: false,\n            question: app.renderMessage('valid-date', {}, \"Please enter a valid date in DD/MM/YYYY HH:MM am/pm format\")\n        });\n    }\n    const dateregex = /^(?:(?:31(\\/|-|\\.)(?:0?[13578]|1[02]))\\1|(?:(?:29|30)(\\/|-|\\.)(?:0?[1,3-9]|1[0-2])\\2))(?:(?:1[6-9]|[2-9]\\d)?\\d{2})$|^(?:29(\\/|-|\\.)0?2\\3(?:(?:(?:1[6-9]|[2-9]\\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\\d|2[0-8])(\\/|-|\\.)(?:(?:0?[1-9])|(?:1[0-2]))\\4(?:(?:1[6-9]|[2-9]\\d)?\\d{2})$/;\n    const timeregex = /^([0-9]|0[0-9]|1[0-2]):[0-5][0-9]$/;\n    const ampmregex = /^(AM|PM)/;\n    if (dateregex.test(splits[0]) && timeregex.test(splits[1]) && ampmregex.test(splits[2])) {\n        let a = value.split(\"/\");\n        let date1 = new Date(a[1] + \"/\" + a[0] + \"/\" + a[2]);\n        let date = new Date();\n        if (date.getTimezoneOffset() == 0) {\n            date = new Date(date.getTime() + 5 * 60 * 60000 + 30 * 60000);\n        }\n        if (date1.getTime() - date.getTime() > 0) {\n            resolve({\n                success: false,\n                question: app.renderMessage('date-error', {}, \"Date and time of accident must be earlier than the current date and time\")\n            });\n        }\n        else {\n            let lossDate = value.split('/');\n            lossDate = lossDate[1]+'/'+lossDate[0]+'/'+lossDate[2]\n            app.setContextParam('date-time', value);\n            app.setContextParam('accident-date-time', lossDate);\n            app.executeFunction('updateCustomerInformation', args = { field: \"dateTime\", value: value });\n            app.pushData({ accident_date_time: lossDate }, app.context.intent);\n            return resolve();\n        }\n    }\n    else {\n        resolve({\n            success: false,\n            question: app.renderMessage('valid-date', {}, \"Please enter a valid date in DD/MM/YYYY HH:MM am/pm format\")\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-17T16:14:11.294Z",
          "email": "parvez@yellowmessenger.com",
          "name": "dateAndTimeValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abbe",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    if(app.data.message === 'Accident Location'){\n        app.pushData({garage_or_not:\"Accident Location\"},app.context.intent);\n        return resolve();\n    }else if(app.data.message === 'garage'){\n        app.pushData({garage_or_not:\"garage\"},app.context.intent);\n        return resolve();\n    }else if(app.data.message === 'With Insured'){\n        app.pushData({garage_or_not:\"With Insured\"},app.context.intent);\n        return resolve();\n    }else{\n        app.sendQuickReplies({\n            title:app.renderMessage('',{},''),\n            options:[\n                {\n                    title:\"Accident\",\n                    text:\"Accident Location\"\n                },\n                {\n                    title:\"Garage\",\n                    title:'garage'\n                },\n                {\n                    title:\"Other\",\n                    text:'With Insured'\n                }\n            ]\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.128Z",
          "email": "parvez@yellowmessenger.com",
          "name": "garageOrnotValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abbf",
          "code": "return new Promise(function (resolve) {\n    if (app.term) {\n        app.memory.get(\"make_id\").then((result) => {\n            app.memory.get(\"vehicle_type\").then((vehicle_type) => {\n                // app.log(result, \"RESULT\");\n                // app.log(vehicle_type, \"VEHICLE TYPE\");\n                app.dataStore.search({\n                    table: \"vehicle_model_new\",\n                    body: {\n                        \"query\": {\n                            \"bool\": {\n                                \"must\": [\n                                    {\n                                        \"regexp\": {\n                                            \"model_name\": app.term.toLowerCase() + \".*\"\n                                            //  \"model_name\": term.toLowerCase() \n                                        }\n                                    },\n                                    {\n                                        \"match\": {\n                                            \"make_id\": result\n                                        }\n                                    },\n                                    {\n                                        \"match\": {\n                                            \"vehicle_type_id_fk\": vehicle_type\n                                        }\n                                    }\n                                ]\n                            }\n                        }\n                    }\n                }).then((result) => {\n                    app.log(result, \"AUto complete result\")\n                    resolve(app._.map(result.hits.hits, function (hit) {\n                        return [hit._source.model_name + \" \" + hit._source.variance, hit._source.model_name + \"$\" + hit._source.model_id + \"$\" + hit._source.variance];\n                    }))\n                })\n\n            })\n        })\n    } else { resolve([]) }\n})",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-28T12:38:38.833Z",
          "email": "parvez@yellowmessenger.com",
          "name": "vehicleModelAutoComplete",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abc0",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    if (app.data.message.length < 3) {\n        return resolve({\n            success: false,\n            question: app.renderMessage('address-validator', {}, '')\n        })\n    } else {\n        app.setContextParam('address', app.data.message).then(() => {\n            app.pushData({ Vehc_Insp_Address: app.data.message }, app.context.intent);\n            return resolve();\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.130Z",
          "email": "parvez@yellowmessenger.com",
          "name": "addressValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abc1",
          "code": "const otpNumbers = () => {\n    return app.sendQuickReplies({\n        title: app.renderMessage(\"enter-otp\", {}, \"Please enter the 4-digit OTP send to your mobile number\"),\n        options: [\n            {\n                title: \"Resend OTP\",\n                text: \"resend otp again\"\n            },\n            {\n                title: \"Change Number\",\n                text: 'change number'\n            }\n        ]\n    })\n}\nconst wrongOtp = () => {\n    return app.sendQuickReplies({\n        title: app.renderMessage(\"wrong-otp\", {}, \"The OTP you have entered is invalid please try again.\"),\n        options: [\n            {\n                title: \"Resend OTP\",\n                text: \"resend otp again\"\n            },\n            {\n                title: \"Change Number\",\n                text: 'change number'\n            }\n        ]\n    })\n}\nreturn new Promise(resolve => {\n    // Your logic goes here\n    const value = app.data.message;\n    if (value === 'change number') {\n        app.setContextParam('mobile-number', undefined);\n        return resolve();\n    } else if (/^\\d{4}$/g.test(value)) {\n        app.verifyOtp(value).then(res => {\n            if (res.success) {\n                app.sendTextMessage(app.renderMessage('otp-verified', {}, \"Your OTP has been successfully verified.\"))\n                return resolve();\n            }else{\n                wrongOtp();\n            }\n        })\n    } else if (value === 'resend otp again'){\n        otpNumbers();\n    } \n    else {\n        otpNumbers();\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.130Z",
          "email": "parvez@yellowmessenger.com",
          "name": "verifyOtp",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abc2",
          "code": "const errorMessage = () => {\n    app.sendTextMessage(app.renderMessage('error-message-mobile', {}, 'There was an error fetching your registered mobile number pelase try again.')).then(() => {\n        app.triggerIntent('default', {});\n        return;\n    })\n}\nreturn new Promise((resolve, reject) => {\n    // Your logic goes here\n    try {\n        const requestBody = `<?xml version=\"1.0\" encoding=\"UTF-8\"?><soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:cus=\"http://stub.unotechsoft.com/wsdl/CustomerService/\"><soapenv:Header /><soapenv:Body><cus:getCustomerByPolicyNo><!--Optional:--><cus:source>TATA-AIG</cus:source><!--Optional:--><cus:medium>CHATBOT</cus:medium><!--Optional:--><cus:campaingn>CHATBOT</cus:campaingn><!--Optional:--><cus:strLVTokenID /><!--Optional:--><cus:strPolicyNo>${args.policyNumber}</cus:strPolicyNo></cus:getCustomerByPolicyNo></soapenv:Body></soapenv:Envelope>`\n        app.requestOptions.uri = app.customerDetails;\n        app.requestOptions.body = requestBody;\n        app.log(app.requestOptions, \"request body in MobileQF\");\n        app.request.request(app.requestOptions, function (err, res, body) {\n            if (err || !res || !body || res.statusCode != 200) {\n                app.log(err, \"Error in response mobileQf\");\n                errorMessage();\n                return resolve();\n            } else {\n                body = JSON.parse(app.xmlToJSON.toJson(body));\n                app.log(body, \"body\")\n                const details = body[\"soap:Envelope\"][\"soap:Body\"];\n                if (details.getCustomerByPolicyNoResponse.GetCustomerByPolicyNoResult['ns2:ID'] && details.getCustomerByPolicyNoResponse.GetCustomerByPolicyNoResult['ns2:ID'] != null && typeof(details.getCustomerByPolicyNoResponse.GetCustomerByPolicyNoResult['ns2:ID']) != 'object') {\n                    return resolve(details.getCustomerByPolicyNoResponse.GetCustomerByPolicyNoResult['ns2:ID']);\n                } else {\n                    return resolve('null');\n                }\n            }\n        })\n\n    } catch (err) {\n        app.log(err, \"ERROR in getMobileNumber-1\");\n        errorMessage();\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.131Z",
          "email": "parvez@yellowmessenger.com",
          "name": "policyDetails",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abc3",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    if (app.data.message.toLowerCase() === 'motor') {\n        return resolve();\n    } else {\n        app.sendTextMessage(app.renderMessage(\"register_non_motor_claim\", {}, `You may register your non motor claim on this link - https://bit.ly/2uWLnmN`)).then(() => {\n            app.triggerIntent('anything-else', {});\n            return;\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-11T18:25:59.080Z",
          "email": "parvez@yellowmessenger.com",
          "name": "claimValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abc4",
          "code": "\nreturn new Promise(resolve => {\n    // Your logic goes here\n    if(app.prediction.global_model.intent === 'yes' && app.prediction.global_model.confidence > 0.85){\n        app.pushData({insured_person:\"yes\"},app.context.intent);\n        return resolve();\n    }else{\n        app.pushData({insured_person:\"no\"},app.context.intent);\n        return resolve();\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.126Z",
          "email": "parvez@yellowmessenger.com",
          "name": "yesNoValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abc5",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.validate(app.data.message).then((result) => {\n        if (!result) {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"ask-name\", {}, \"Please tell me your name\")\n            })\n        } else {\n            app.setContextParam('cust-name', result);\n            app.profile.username = result;\n            app.updateProfile();\n            let data = { username: result, transaction: \"Abandoned\" }\n            if (app.context.intent === 'renewal-policy') {\n                app.setContextParam('doc_type', 'Renewal Notice$');\n                data.doc_type = 'Renewal Notice$'\n            } else if (app.context.intent === 'buy-online' || app.context.intent === 'others' || app.context.intent === 'customer-care') {\n                data = { name: result, transaction: \"Abandoned\" };\n            }\n            app.pushData(data, app.context.intent);\n            app.executeFunction('updateCustomerInformation', args = { field: \"name\", value: result });\n            return resolve();\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-25T08:15:31.472Z",
          "email": "parvez@yellowmessenger.com",
          "name": "nameValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abc6",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const result = app.data.message.split('$');\n    if (result.length < 2 || result.length > 2) {\n        return resolve({\n            success: false,\n            question: app.renderMessage('city', {}, \"\")\n        })\n    } else {\n        app.setContextParam('cur-city-id', result[1]).then(() => {\n            app.setContextParam('cur-city-name', result[0]).then(() => {\n                if (app.context.intent === 'claim-intimation') {\n                    app.pushData({ cur_city: result[0] }, app.context.intent);\n                    return resolve();\n                } else {\n                    app.pushData({ CityValue: result[0] }, app.context.intent);\n                    return resolve();\n                }\n            })\n        })\n    }\n});\n",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-11T11:32:45.514Z",
          "email": "parvez@yellowmessenger.com",
          "name": "claimCurrentCityValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abc7",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.pushData({ cur_landmark: app.data.message }, app.context.intent);\n    return resolve();\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-11T08:47:49.545Z",
          "email": "parvez@yellowmessenger.com",
          "name": "claimCurrentLandmardValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abc8",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.validate(app.data.message).then((result) => {\n        if (!result) {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"ask-name\", {}, \"Please tell me your name\")\n            })\n        } else {\n            app.setContextParam('cust-name', result);\n            let data = { InsurerName: result, transaction: \"Abandoned\" };\n            app.pushData(data, app.context.intent);\n            app.executeFunction('updateCustomerInformation', args = { field: \"name\", value: result });\n            return resolve();\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-15T10:50:27.679Z",
          "email": "parvez@yellowmessenger.com",
          "name": "agentNameValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abc9",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    let vehNumber = app.data.message.replace(/[^A-Z0-9]/ig, \"\");\n    vehNumber = vehNumber.toLowerCase();\n    if (vehNumber.length > 5) {\n        app.setContextParam('reg-number',vehNumber);\n        app.pushData({ VehicleRegNo: vehNumber }, app.context.intent);\n        return resolve();\n    }else{\n        return resolve({\n            success:false,\n            question:app.renderMessage('wrong-reg',{},\"\")\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-17T07:01:58.413Z",
          "email": "parvez@yellowmessenger.com",
          "name": "registrationNumberValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abca",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.validate(app.data.message).then((result) => {\n        if (!result) {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"email-validator\", {}, \"Please enter a valid email id\")\n            })\n        } else if (/^(([^<>()\\[\\]\\\\.,;:\\s@\"]+(\\.[^<>()\\[\\]\\\\.,;:\\s@\"]+)*)|(\".+\"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,}))$/g.test(result)) {\n            result = result.toLowerCase();\n            app.setContextParam('email-id', result);\n            app.pushData({ ProposerEmailId: result }, app.context.intent)\n            app.executeFunction('updateCustomerInformation', args = { field: \"email\", value: result });\n            return resolve();\n        } else {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"email-validator\", {}, \"Please enter a valid email id\")\n            })\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-19T11:33:48.226Z",
          "email": "parvez@yellowmessenger.com",
          "name": "agentEmailValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abcb",
          "code": "const errorMessage = (data, requestBody, responseBody, error, elapsedTime) => {\n    app.pushData({ transaction: 'Failed' }, app.context.intent);\n    app.executeFunction('crmApi', args = { data: data, status: 'Closed', intentName: \"preinspection-request\" });\n    app.executeFunction('apiResponseDatabase', args = { request: requestBody, response: responseBody, error: error, tableName: \"preinspection_api_database\", \"type\": \"Lead Creation\", \"elapsedTime\":elapsedTime })\n    return app.sendTextMessage(app.renderMessage('preinspection-error', {}, \"There was some error while processing your preinspection request. Pelase try again.\")).then(() => {\n        app.clearContext();\n        app.data.message = 'help';\n        return app.start();\n    })\n};\n\nconst onSuccess = (data, requestBody, responseBody, error, elapsedTime) => {\n    app.pushData(\n        {\n            LeadId: responseBody.LeadID,\n            InspectionAgentName: responseBody.SMCodeValue,\n            VendorCode: responseBody.VendorCode,\n            SMCode: responseBody.SMCode,\n            RGICL_OfficeValue: responseBody.RGICL_OfficeValue,\n            transaction: \"Success\",\n            elapsed_time: elapsedTime,\n        }, app.context.intent);\n    data.leadId = responseBody.LeadID;\n    app.executeFunction('crmApi', args = { data: data, status: 'Closed', intentName: \"preinspection-request\" });\n    app.executeFunction('apiResponseDatabase', args = { request: requestBody, response: responseBody, error: error, tableName: \"preinspection_api_database\", \"type\": \"Lead Creation\", \"elapsedTime\":elapsedTime  });\n    app.memory.delete('preinspection_leads_id');\n}\n\nconst ERROR_MSG = \"ERROR MESSAGE\"\nreturn new Promise((resolve, reject) => {\n    const steps = args.steps;\n    const agent = args.agent;\n    const name = args.steps['insured-name'].split(' ');\n    let email = args.steps['secondary-email'] === 'noemailid' ? steps['email-id'] : steps['email-id'] + ', ' + steps['secondary-email'];\n    const empty_string = \"\";\n    // app.sendTextMessage(steps['vehicle-type'])\n    const userData = {\n        email: \"\",\n        mobileNo: steps['insured-mobile'],\n        policyNo: \"\",\n        username:args.steps['insured-name'],\n        leadId:\"\",\n        callerRelation:\"Prospect\",\n        product:steps['vehicle-type'] === 'Two-Wheeler$4' ? '3122': '3121'\n    }\n    try {\n        let reqBody = {\n            \"CustomerFname\": name.length == 1 ? name[0] : name[0],\n            \"CustomerMname\": name.length >= 3 ? name[1] : \"\",\n            \"CustomerLname\": name.length == 2 ? name[1] : name.length >= 3 ? name.slice(2).join(\" \") : \"\",\n            \"CustomerAddress1\": steps['address'] == null ? \"\" : steps['address'],\n            \"CustomerAddress2\": empty_string,\n            \"CustomerAddress3\": empty_string,\n            \"CustomerContactNo\": steps['insured-mobile'] == null ? empty_string : steps['insured-mobile'],\n            \"CustomerTelephoneNo\": empty_string,\n            \"VendorCode\": agent.inspection_agent_name,\n            \"VendorCodeValue\": agent.inspection_agent_name,\n            \"BasCode\": empty_string,\n            \"BasCodeValue\": empty_string,\n            \"BasMobile\": empty_string,\n            \"SMCode\": agent.manager_name,\n            \"SMCodeValue\": agent.manager_name,\n            \"SMMobileNo\": \"9876543210\",\n            \"vehicletype\": steps['vehicle-type'].split(\"$\")[1] == null ? empty_string : steps['vehicle-type'].split(\"$\")[1],\n            \"vehicletypeValue\": steps['vehicle-type'].split(\"$\")[0] == null ? empty_string : steps['vehicle-type'].split(\"$\")[0],\n            \"vehicleRegNo\": steps['reg-number'] == null ? empty_string : steps['reg-number'],\n            \"Make\": steps['make-id'] == null ? empty_string : steps['make-id'],\n            \"MakeValue\": steps['make-name'] == null ? empty_string : steps['make-name'],\n            \"Model\": steps['model-id'] == null? empty_string : steps['model-id'],\n            \"ModelValue\": steps['model-name'] == null ? empty_string : steps['model-name'],\n            \"EngineNo\": empty_string,\n            \"ChassisNo\": empty_string,\n            \"State\": steps['state-id'] == null ? empty_string : steps['state-id'],\n            \"stateValue\": steps['state-name'] == null ? empty_string : steps['state-name'],\n            \"District\": steps['district-id'] == null ? empty_string : steps['district-id'],\n            \"Districtvalue\": steps['district-name'] == null ? empty_string : steps['district-name'],\n            \"city\": steps['city-id'] == null ? empty_string : steps['city-id'],\n            \"cityValue\": steps['city-name'] == null ? empty_string : steps['city-name'],\n            \"pincode\": steps.pincode,\n            \"RGICL_Office\": steps['district-id'] == null ? empty_string : steps['district-id'],\n            \"RGICL_OfficeValue\": steps['district-name'] == null ? empty_string : steps['district-name'],\n            \"Vech_Insp_Address\": steps['address'] == null ? \"\" : steps['address'],\n            \"Vech_Insp_Address2\": empty_string,\n            \"Vech_Insp_Address3\": empty_string,\n            \"Remark\": \"good\",\n            \"LeadType\": \"1\",\n            \"state_Veh\": steps['state-id'] == null ? empty_string : steps['state-id'],\n            \"stateValue_veh\": steps['state-name'] == null ? empty_string : steps['state-name'],\n            \"District_Veh\": steps['district-id'] == null ? empty_string : steps['district-id'],\n            \"Districtvalue_Veh\": steps['district-name'] == null ? empty_string : steps['district-name'],\n            \"city_Veh\": steps['city-id'] == null ? empty_string : steps['city-id'],\n            \"cityValue_Veh\": steps['city-name'] == null ? empty_string : steps['city-name'],\n            \"pincode_Veh\": \"400025\",\n            \"ProposerName\": empty_string,\n            \"ObjectiveOfInspection\": \"8\",\n            \"ObjectiveOfInspectionValue\": \"PolicyBooking\",\n            \"InspectionToBeDone\": \"8\",\n            \"InspectionToBeDoneValue\": \"PolicyBooking\",\n            \"LeadCreatedBy\": \"CHATBOT\",\n            \"LeadCreatedbySystem\": \"6\",\n            \"IntimatorName\": \"Sales Manager 1\",\n            \"IntimatorMobileNo\": \"9876543210\",\n            \"InsurerCode\": \"1001\",\n            \"InsurerName\": \"Tata AIG\",\n            \"LeadCreationFor\": \"Pre-Inspection\",\n            \"ProposerAgentMobile\": steps['agent-mobile'],\n            \"ProposerEmailId\": email,\n            \"AgencyId\": \"1\",\n            \"ManagerName\": agent.manager_name,\n            \"InspectionAgentName\": agent.inspection_agent_name\n\n        };\n        app.preinspectionRequest.url = app.preinspectionRequest.url + 'SetCreateLead';\n        app.preinspectionRequest.body = reqBody;\n        app.log(app.preinspectionRequest, \"options in preinspection request\");\n        const startTime = new Date();\n        app.request.request(app.preinspectionRequest, (error, response, body) => {\n            app.elapsedTime(startTime).then(elapsed => {\n                response.elapsedTime = elapsed;\n                app.log(response, \"RESPONSE IN Preinspection\")\n                if (error || response.statusCode !== 200) {\n                    errorMessage(userData, app.preinspectionRequest, body, error, elapsed);\n                    reject(error);\n                } else if (body) {\n                    if (body && body.LeadID) {\n                        onSuccess(userData, app.preinspectionRequest, body, error, elapsed);\n                        resolve(body);\n                    } else {\n                        errorMessage(userData, app.preinspectionRequest, body, error, elapsed);\n                        reject(ERROR_MSG);\n                    }\n                } else {\n                    errorMessage(userData, app.preinspectionRequest, body, error, elapsed);\n                    reject(ERROR_MSG);\n                }\n            });\n        });\n    } catch (e) {\n        app.log(e, \"ERROR in catchPreinspection\")\n        errorMessage(userData, app.preinspectionRequest, body, e);\n        reject(e);\n    }\n\n}, (msg) => {\n    errorMessage(userData, app.preinspectionRequest, body, msg);\n    reject(msg);\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-15T14:25:33.789Z",
          "email": "parvez@yellowmessenger.com",
          "name": "preinspectionRequestApi",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abcc",
          "code": "return new Promise(resolve => {\n    if (!(/^\\d{6}$/g.test(app.data.message))) {\n        return resolve({\n            success: false,\n            question: app.renderMessage(\"incorrect_lead\", {}, \"Please enter a valid lead number\")\n        })\n    } else {\n        app.pushData({ lead_id: app.data.message }, app.context.intent);\n        return resolve();\n    }\n})",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-05T06:29:33.694Z",
          "email": "parvez@yellowmessenger.com",
          "name": "leadNumberValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abcd",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    if (app.prediction.global_model.intent === 'no' && app.prediction.global_model.confidence > 0.85) {\n        app.pushData({ reg_no: \"Don't have regitration number\" }, app.context.intent);\n        return resolve();\n    } else {\n        const vehicleNo = app.data.message.replace(/[^A-Z0-9]/ig, \"\").toLowerCase();\n        if (vehicleNo.length>5) {\n            app.executeFunction('updateCustomerInformation', args = { field: \"regNo\", value: vehicleNo });\n            app.pushData({ reg_no: vehicleNo }, app.context.intent);\n            return resolve();\n        } else {\n            app.sendQuickReplies({\n                title: app.renderMessage('ask-reg-no', {}, \"\"),\n                options: [\n                    {\n                        title: app.renderMessage('reg-no', {}, ''),\n                        text: \"no\"\n                    },\n                ]\n            });\n        }\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-11T11:11:32.061Z",
          "email": "parvez@yellowmessenger.com",
          "name": "regValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abce",
          "code": "const askName = () => {\n    return app.sendTextMessage(app.renderMessage('insured-phone-number',{},'Please enter your 10 digit mobile number'));\n}\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    app.memory.get('userDetails').then(user => {\n        user = JSON.parse(user);\n        if (user.insuredMobile) {\n            app.sendQuickReplies({\n                title: app.renderMessage('insured-phone-number',{},\"Please enter your 10 digit mobile number\"),\n                options: [{\n                    title: user.insuredMobile,\n                    text: user.insuredMobile\n                }]\n            });\n            return resolve();\n        } else {\n            askName()\n            return resolve();\n        }\n    }).catch(err => {\n        askName()\n        return resolve();\n    })\n\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.132Z",
          "email": "parvez@yellowmessenger.com",
          "name": "claimInsuredMobileQf",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abcf",
          "code": "\nreturn new Promise(resolve => {\n    // Your logic goes here\n    if(app.prediction.global_model.intent === 'yes' && app.prediction.global_model.confidence > 0.85){\n        app.pushData({declaration:\"yes\"},app.context.intent);\n        return resolve();\n    }else{\n        app.sendQuickReplies({\n            title:app.renderMessage('consent-error',{},''),\n            options:[\n                {\n                    title:'I consent',\n                    text:'yes'\n                }\n            ]\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.137Z",
          "email": "parvez@yellowmessenger.com",
          "name": "declarationValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abd0",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.validate(app.data.message).then(policy => {\n        if (/^[012345]\\d{9}$/g.test(policy)) {\n            app.executeFunction('updateCustomerInformation', args = { field: \"policy\", value: policy });\n            app.setContextParam('policy-number', policy);\n            if (app.context.intent === 'claim-intimation') {\n                let args = {\n                    es_query: {\n                        query: {\n                            match: {\n                                policy_number: policy\n                            }\n                        }\n                    },\n                    table: \"claim_intimation_lead\"\n                }\n                app.executeFunction('searchQuery', args = args).then((result) => {\n                    let condition = new Date(new Date(result.updatedDate).getTime() + 60 * 60 * 24 * 1000) > new Date();\n                    if (result && result.policy_number === policy && result.transaction !== 'Abondened' && condition && !app.UAT_ENV) {\n                        app.sendTextMessage(app.renderMessage('claim-already-registered', { policyNo: result.policy_number}, '')).then(() => {\n                            app.triggerIntent('anything-else', {});\n                            return resolve;\n                        })\n                    } else {\n                        app.pushData({ policy_number: policy, transaction:'Abondened', claim_category:app.context.steps['claim-category'], motor_type: app.context.steps['motor-type']}, app.context.intent)\n                        return resolve();\n                    }\n                })\n            } else {\n                app.pushData({ policy_number: policy }, app.context.intent)\n                return resolve();\n            }\n        } else {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"incorrect_policy_number\", {}, \"Please enter a valid 10 digit policy number. \\n(for eg: 0155009013)\")\n            })\n        }\n    });\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-02T07:30:53.848Z",
          "email": "parvez@yellowmessenger.com",
          "name": "paymentPolicyValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abd1",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const result = app.data.message.split('$');\n    if (result.length < 2 || result.length>2) {\n        return resolve({\n            success: false,\n            question: app.renderMessage('vehicle-make', {}, \"\")\n        })\n    } else {\n        app.setContextParam('make-name', result[0]).then(() => {\n            app.memory.set('make_id',result[1]);\n            app.setContextParam('make-id', result[1]).then(() => {\n                app.pushData({ MakeValue: app.data.message }, app.context.intent);\n                return resolve();\n            })\n        })\n    }\n});\n",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.139Z",
          "email": "parvez@yellowmessenger.com",
          "name": "vehicleMakeValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abd2",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    try {\n        app.validate(app.data.message).then((result) => {\n            if (!result) {\n                return resolve({\n                    success: false,\n                    question: app.renderMessage(\"policy-number\", {}, \"Please enter a 10 digit policy number\")\n                })\n            } else if (/^[012]\\d{9}$/g.test(result)) {\n                app.setContextParam('policy-number', result);\n                app.executeFunction('updateCustomerInformation', args = { field: \"policy\", value: result });\n                app.executeFunction('getMobileNumber', args = {\"policyNumber\":result}).then((mobileNumbers) => {\n                    if (!mobileNumbers) {\n                        return resolve({\n                            success: false,\n                            question: app.renderMessage('wrong-policy', {}, \"The poilcy you have entered is not available in TATA AIG please verify it and try agian.\")\n                        })\n                    } else {\n                        app.log(mobileNumbers,\"Mobile numbers\");\n                        app.pushData({\"policy_number\":result}, app.context.intent);\n                        app.executeFunction('updateCustomerInformation', args = { field: \"mobile\", value: mobileNumbers });\n                        return resolve();\n                    }\n                })\n            } else {\n                return resolve({\n                    success: false,\n                    question: app.renderMessage(\"policy-number\", {}, \"Please enter a 10 digit policy number\")\n                })\n            }\n        })\n    } catch (err) {\n        app.log(err, \"ERROR\");\n        app.sendTextMessage(app.renderMessage('calim-error',{},\"\"))\n        app.triggerIntent('anything-else',{});\n        return;\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-30T06:18:39.108Z",
          "email": "tagic12@tagic.com",
          "name": "policyNumberValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abd3",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.memory.get('selectedLanguage').then((result) => {\n        app.options.targetLanguage = result;\n        app.triggerIntent('services', {}).then(() => {\n            return resolve();\n        })\n    }).catch(err => {\n        app.sendTextMessage(app.renderMessage('tara', {}, \"\")).then(() => {\n            app.memory.get('selectedLanguage').then(result => {\n                app.options.targetLanguage = result;\n                app.triggerIntent('change-language', {}).then(() => {\n                    return resolve();\n                })\n            }).catch(err => {\n                app.triggerIntent('change-language', {}).then(() => {\n                    return resolve();\n                })\n            })\n        })\n    });\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-06T18:22:27.885Z",
          "email": "parvez@yellowmessenger.com",
          "name": "defaultPromptFunction",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abd4",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const value = app.data.message;\n    const arry = ['OD', 'Key', 'tyre', 'stolen', 'parked'];\n    if (arry.includes(value)) {\n        app.pushData({ claim_type: value }, app.context.intent);\n        if (value === 'parked') {\n            app.setContextParam('driver-name', \"Vehicle was parked\").then(() => {\n                app.setContextParam('license-no', \"Vehicle was parked\").then(() => {\n                    app.setContextParam('vehicleParked', 'Yes');\n                    app.pushData({ driver_name: \"Vehicle was parked\", license_no: \"Vehicle was parked\" }, app.context.intent)\n                    return resolve();\n                })\n            })\n        } else {\n            return resolve();\n        }\n    } else {\n        if (app.context.steps['motor-type'] === '4') {\n            app.sendQuickReplies({\n                title: app.renderMessage('buy-online-type', {}, ''),\n                options: [\n                    {\n                        title: 'Vehicle Damage',\n                        text: 'OD'\n                    },\n                    {\n                        title: 'Key Loss',\n                        text: 'Key'\n                    },\n                    {\n                        title: 'Tyre Damage',\n                        text: 'tyre'\n                    },\n                    {\n                        title: 'Parked and Vehicle Damage',\n                        text: 'parked'\n                    },\n\n                ]\n            })\n        } else {\n            app.sendQuickReplies({\n                title: app.renderMessage('buy-online-type', {}, ''),\n                options: [\n                    {\n                        title: 'Vehicle Damage',\n                        text: 'OD'\n                    },\n                    {\n                        title: 'Parked and Vehicle Damage',\n                        text: 'parked'\n                    },\n\n                ]\n            })\n        }\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-17T09:13:04.883Z",
          "email": "parvez@yellowmessenger.com",
          "name": "claimTypeValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abd5",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.pushData({ loss_landmark: app.data.message }, app.context.intent);\n    return resolve();\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-11T08:48:02.538Z",
          "email": "parvez@yellowmessenger.com",
          "name": "lossLandMarkValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abd6",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const result = app.data.message.split('$');\n    if (result.length < 2 || result.length > 2) {\n        return resolve({\n            success: false,\n            question: app.renderMessage('district', {}, \"\")\n        })\n    } else {\n        app.setContextParam('cur-district-id', result[1]).then(() => {\n            app.memory.set('district_id', result[1]);\n            app.setContextParam('cur-district-name', result[0]).then(() => {\n                if (app.context.intent === 'claim-intimation') {\n                    app.pushData({ current_district: result[0] }, app.context.intent);\n                    return resolve();\n                } else {\n                    app.pushData({ DistrictValue: result[0] }, app.context.intent);\n                    return resolve();\n                }\n            })\n        })\n    }\n});\n",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-11T11:33:15.413Z",
          "email": "parvez@yellowmessenger.com",
          "name": "claimCurrentdistrictValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abd7",
          "code": "const errorMessage = (data, requestBody, responseBody, error) => {\n    app.executeFunction('crmApi', args = { data: data, status: 'Open', intentName: app.context.intent }).then((ticketNumber) => {\n        app.executeFunction('apiResponseDatabase', args = { request: requestBody, response: responseBody, error: error, ticketNumber: ticketNumber, tableName: \"policy_document_api_database\", \"type\": \"Policy Soft Copy\" });\n        app.pushData({ transaction: 'Failed', ticket: ticketNumber }, app.context.intent).then(() => {\n            app.memory.delete('policy_document_lead_id');\n            return app.sendTextMessage(app.renderMessage('document-error', {}, \"There was some error fetching your document pelase try again.\")).then(() => {\n                app.clearContext();\n                app.data.message = 'help';\n                return app.start();\n            })\n        })\n    })\n}\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    try {\n\n        const steps = app.context.steps;\n        let dataToBeStored = {\n            subquery: 'Policy Soft Copy',\n            docType: steps.doc_type,\n            policyNo: steps['policy-number'],\n            mobileNo: steps['mobile'],\n            email: steps['email-id'],\n            username: steps['cust-name'],\n            assignedTo: \"ois_raviuda\"\n        }\n        const requestBody = `\n    <soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:chat=\"http://stub.unotechsoft.com/wsdl/ChatbotService/\" xmlns:com=\"http://stub.unotechsoft.com/wsdl/CommercialVehicleLiteService/\">\n        <soapenv:Header/>\n        <soapenv:Body>\n            <chat:getDocumentList>\n                <com:source>TATA-AIG</com:source>\n                <com:medium>CHATBOT</com:medium>\n                <com:campaign>CHATBOT</com:campaign>\n                <com:strServiceToken></com:strServiceToken>\n                <chat:PolicyNumber>${dataToBeStored.policyNo}</chat:PolicyNumber>\n                <chat:GCSource>chat bot</chat:GCSource>\n                <chat:DocumentType>${dataToBeStored.docType}</chat:DocumentType>\n            </chat:getDocumentList>\n        </soapenv:Body>\n    </soapenv:Envelope>`;\n        app.requestOptions.body = requestBody;\n        app.requestOptions.url = app.policyUrl;\n        app.request.request(app.requestOptions, function (err, res, body) {\n            if (err || !res || !body) {\n                errorMessage(dataToBeStored, app.requestOptions, res, err);\n            } else if (body) {\n                try {\n                    body = JSON.parse(app.xmlToJSON.toJson(body));\n                    if (body && body[\"soap:Envelope\"] && body[\"soap:Envelope\"][\"soap:Body\"] && body[\"soap:Envelope\"][\"soap:Body\"][\"ns2:getDocumentListResponse\"] && body[\"soap:Envelope\"][\"soap:Body\"][\"ns2:getDocumentListResponse\"][\"ns2:ChatbotResult\"]) {\n                        body = JSON.parse(app.xmlToJSON.toJson(body[\"soap:Envelope\"][\"soap:Body\"][\"ns2:getDocumentListResponse\"][\"ns2:ChatbotResult\"]));\n                        if (body && body['Documents'] && body[\"Documents\"]['Document'] && body[\"Documents\"]['Document']['ByteStream']) {\n                            body = body[\"Documents\"][\"Document\"][\"ByteStream\"];\n                            app.executeFunction('crmApi', args = { data: dataToBeStored, status: 'Closed', intentName: app.context.intent }).then((ticketNumber) => {\n                                app.pushData({ transaction: \"Success\", ticket_number: ticketNumber }, app.context.intent).then(() => {\n                                    app.memory.delete('policy_document_lead_id');\n                                });\n                                app.executeFunction('apiResponseDatabase', args = { request: app.requestOptions, response: \"File Downloaded\", error: err, ticketNumber: ticketNumber, tableName: \"policy_document_api_database\", \"type\": \"Policy Soft Copy\" });\n                            }).then(() => {\n                                if (app.source === 'facebook') {\n                                    app.sendTextMessage('here')\n                                    app.sendEmail('parvez@yellowmessenger.com', \"PDF\", \"This is attachment\", [{filename: 'policy.pdf', content: body}], 'tara@yellowmessenger.com')\n                                } else {\n                                    app.sendEvent({\n                                        code: \"pdf\",\n                                        data: {\n                                            body: body,\n                                            doc_name: dataToBeStored.policyNo + \" \" + dataToBeStored.docType\n                                        }\n                                    });\n                                    return resolve();\n                                }\n                            })\n                        } else {\n                            errorMessage(dataToBeStored, app.requestOptions, res, err);\n                        }\n                    } else {\n                        errorMessage(dataToBeStored, app.requestOptions, res, err);\n                    }\n                } catch (err) {\n                    app.log(err, \"ERROR in policyDocument Api response\")\n                    errorMessage(dataToBeStored, app.requestOptions, body, err.stack)\n                }\n            } else {\n                errorMessage(dataToBeStored, app.requestOptions, res, err);\n            }\n\n        });\n\n    } catch (err) {\n        app.log(err, \"ERROR -22-policydocumentAction\");\n        app.triggerIntent('anything-else', {});\n        return;\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-09T18:21:22.513Z",
          "email": "parvez@yellowmessenger.com",
          "name": "policyDocumentAction",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abd8",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    if (app.prediction.global_model.intent === 'yes' && app.prediction.global_model.confidence > 0.85) {\n        return resolve();\n    } else if (app.prediction.global_model.intent === 'no' && app.prediction.global_model.confidence > 0.85) {\n        app.sendTextMessage(app.renderMessage('agent',{},\"\")).then(()=>{\n            app.sendTextMessage(app.renderMessage('urgency',{},\"\")).then(()=>{\n                app.triggerIntent('anything-else',{});\n                return;\n            })\n        })\n    } else {\n        app.sendTextMessage(app.renderMessage('doc-type', {}, 'Please choose from the below options')).then(() => {\n            app.sendQuickReplies({\n                title: app.renderMessage('agent-service', {}, ''),\n                options: [\n                    {\n                        title: 'Yes',\n                        text: 'yes'\n                    },\n                    {\n                        title: 'No',\n                        text: 'no'\n                    }\n                ]\n            })\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.142Z",
          "email": "parvez@yellowmessenger.com",
          "name": "checkAgentValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abd9",
          "code": "return new Promise(function (resolve) {\n    if (app.term) {\n        app.memory.get(\"district_id\").then(district_id => {\n            console.log(district_id, \"DISTRICT ID\");\n            app.dataStore.search({\n                table: \"cities\",\n                body: {\n                    \"query\": {\n                        \"bool\": {\n                            \"must\":\n                            { \"regexp\": { \"city_name\": app.term.toLowerCase() + \".*\" } }\n                            ,\n                            \"filter\":\n                            {\n                                \"match\": { \"city_fk\": district_id },\n                            }\n                        }\n                    }\n                }\n            }).then((result) => {\n                resolve(app._.map(result.hits.hits, function (hit) {\n                    return [hit._source.city_name, hit._source.city_name + \"$\" + hit._source.city_id];\n                }))\n\n            }, (e) => {\n                app.log(e, \"error\");\n            })\n        })\n    } else { resolve([]) }\n})",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.135Z",
          "email": "parvez@yellowmessenger.com",
          "name": "cityAutoComplete",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abda",
          "code": "const errorMessage = () => {\n    app.sendTextMessage(app.renderMessage('error-message-mobile', {}, 'There was an error fetching your registered mobile number pelase try again.')).then(() => {\n        app.triggerIntent('default', {});\n        return;\n    })\n}\nreturn new Promise(resolve => {\n    // Your logic goes here\n    try {\n        const requestBody = `<?xml version=\"1.0\" encoding=\"UTF-8\"?><soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:cus=\"http://stub.unotechsoft.com/wsdl/CustomerService/\"><soapenv:Header /><soapenv:Body><cus:getCustomerByPolicyNo><!--Optional:--><cus:source>TATA-AIG</cus:source><!--Optional:--><cus:medium>CHATBOT</cus:medium><!--Optional:--><cus:campaingn>CHATBOT</cus:campaingn><!--Optional:--><cus:strLVTokenID /><!--Optional:--><cus:strPolicyNo>${args.policyNumber}</cus:strPolicyNo></cus:getCustomerByPolicyNo></soapenv:Body></soapenv:Envelope>`\n        app.requestOptions.uri = app.customerDetails;\n        app.requestOptions.body = requestBody;\n        app.log(app.requestOptions, \"request body in MobileQF\");\n        app.request.request(app.requestOptions, function (err, res, body) {\n            app.executeFunction('apiResponseDatabase', args = { request: app.requestOptions, response: body, error: err, tableName: \"policy_details_api_database\" });\n            if (err || !res || !body || res.statusCode != 200) {\n                app.log(err, \"Error in response mobileQf\");\n                errorMessage();\n                return;\n            } else {\n                body = JSON.parse(app.xmlToJSON.toJson(body));\n                app.log(body, \"body\")\n                const details = body[\"soap:Envelope\"][\"soap:Body\"];\n                if (details[\"getCustomerByPolicyNoResponse\"] && details[\"getCustomerByPolicyNoResponse\"][\"GetCustomerByPolicyNoResult\"] && (details[\"getCustomerByPolicyNoResponse\"][\"GetCustomerByPolicyNoResult\"][\"ns2:MailLocation\"])) {\n                    const contactDetails = details[\"getCustomerByPolicyNoResponse\"][\"GetCustomerByPolicyNoResult\"][\"ns2:MailLocation\"];\n                    let mobile = {\n                        mobile1: \"\",\n                        mobile2: \"\"\n                    };\n                    // mobile[\"mobile1\"] = contactDetails['ns2:ContactDetails'] && contactDetails[\"ns2:ContactDetails\"][\"ns2:MobileNo\"] ? contactDetails[\"ns2:ContactDetails\"][\"ns2:MobileNo\"] : \"\";\n                    if (contactDetails['ns2:ContactDetails'] && contactDetails[\"ns2:ContactDetails\"][\"ns2:MobileNo\"] && /^\\d{10}/.test(contactDetails[\"ns2:ContactDetails\"][\"ns2:MobileNo\"])) {\n                        mobile[\"mobile1\"] = contactDetails[\"ns2:ContactDetails\"][\"ns2:MobileNo\"];\n                    }\n                    if (contactDetails['ns2:ContactDetails'] && contactDetails[\"ns2:ContactDetails\"][\"ns2:AlternateMobileNo\"] && /^\\d{10}/.test(contactDetails[\"ns2:ContactDetails\"][\"ns2:AlternateMobileNo\"])) {\n                        mobile[\"mobile2\"] = contactDetails[\"ns2:ContactDetails\"][\"ns2:AlternateMobileNo\"];\n                    }\n                    return resolve(mobile);\n                } else {\n                    return resolve(false);\n                }\n            }\n        })\n\n    } catch (err) {\n        app.log(err, \"ERROR in getMobileNumber-1\");\n        errorMessage();\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-09T18:16:10.543Z",
          "email": "parvez@yellowmessenger.com",
          "name": "getMobileNumber",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abdb",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.validate(app.data.message).then((result) => {\n        if (!result) {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"phone-validator\", {}, \"Please enter a valid 10 digit mobile number\")\n            })\n        } else if (/^[6,7,8,9]\\d{9}$/ig.test(result)) {\n            result = result.toLowerCase();\n            app.setContextParam('insured-mobile', result);\n            app.pushData({ CustomerContactNo: result }, app.context.intent)\n            return resolve();\n        } else {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"phone-validator\", {}, \"Please enter a valid 10 digit mobile number\")\n            })\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.135Z",
          "email": "parvez@yellowmessenger.com",
          "name": "insuredNamePhone",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abdc",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    if (app.prediction.entities.language && app.prediction.entities.language[0].text ) {\n        app.setContextParam('select-language', app.prediction.entities.language[0].text);\n        return resolve();\n    } else if( /^.*(hindi|english).*$/ig.test(app.data.message)){\n        app.setContextParam('select-language', app.data.message);\n        return resolve();\n    }else{\n        return resolve();\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.143Z",
          "email": "parvez@yellowmessenger.com",
          "name": "languageInit",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abdd",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    let value = app.data.message;\n    value = value.replace(/[^A-Z0-9]/ig, \"\");\n    value = value.toUpperCase();\n    const regex = /^[A-Z0-9]+$/;\n    if (regex.test(value)) {\n        app.pushData({license_no:value},app.context.intent);\n        app.executeFunction('updateCustomerInformation', args = { field: \"licence\", value: value });\n        return resolve();\n    }\n    else {\n        resolve({\n            success: false,\n            question: app.renderMessage('licence-number',{},\"Please enter a valid licence number\")\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-11T08:43:28.469Z",
          "email": "parvez@yellowmessenger.com",
          "name": "licenceValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abde",
          "code": "// Your code goes here\nlet toTitleCase = (str) => {\n    return str.replace(/\\w\\S*/gi, function (txt) { return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase(); });\n}\nconst callAgent = (userName, userPhone, userEmail) => {\n    return new Promise(resolve => {\n        let issueString = \"Phone : \" + userPhone;\n        app.sendTextMessage(app.renderMessage('agent-wait', {}, \"Please wait while I contact my support center...\")).then(() => {\n            app.raiseTicket({\n                issue: issueString,\n                contact: {\n                    phone: userPhone,\n                    name: userName,\n                    email: userEmail\n                },\n                priority: 'MEDIUM',\n                manualAssignment: true,\n                category: 'buyonline'\n            }).then(function (ticketData) {\n                if (ticketData && ticketData.assignedTo) {\n                    app.log(ticketData, \"Ticket data\");\n                    app.executeFunction('ocrmApi', { status: 'Closed', data: { username: userName, email: userEmail, mobileNo: userPhone, leadId: app.context.steps['type'] } });\n                    app.pushData({ 'assign_to': ticketData.assignedTo, transaction: \"Success\", link: app.getSessionMessageLogUrl() }, app.context.intent).then(() => {\n                        app.memory.delete('buy_online_leads_id');\n                    })\n                    app.sendTextMessage(app.renderMessage('buy-line-support', { agent: ticketData.assignedTo }, \"Our customer support team will assist you shortly...\")).then(() => {\n                        app.pauseBot();\n                    })\n                    return resolve();\n                    //app.sendTextMessage(\"Our agent will assist you. Please wait while we connect you to our agent.\");\n                } else {\n                    app.sendTextMessage(app.renderMessage('agents-not-available', {}, '')).then(() => {\n                        app.executeFunction('ocrmApi', { status: 'Open', data: { username: userName, email: userEmail, mobileNo: userPhone, leadId: app.context.steps['type'] } });\n                        app.pushData({ 'assign_to': \"Agent was offiline\", transaction: \"Failed\", link: app.getSessionMessageLogUrl() }, app.context.intent).then(() => {\n                            app.memory.delete('buy_online_leads_id')\n                        })\n                        app.triggerIntent('anything-else', {});\n                        return resolve();\n                    })\n                }\n            });\n        });\n    })\n}\n\nreturn new Promise((resolve, reject) => {\n    app.memory.get('userDetails').then((result) => {\n        let userDetials = JSON.parse(result);\n        app.log(userDetials, \"UserDetails in connect agent\");\n        callAgent(userDetials.name, userDetials.agentMobile, userDetials.email).then(() => {\n            return resolve();\n        })\n    }).catch(err => {\n        app.log(err, \"ERROR in connect agent\");\n        callAgent('', '', '').then(() => {\n            return resolve();\n        })\n    });\n})",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-05T12:45:25.106Z",
          "email": "parvez@yellowmessenger.com",
          "name": "buyOnline",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abdf",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const steps = app.context.steps;\n    let args = {\n        'es_query': {\n            \"query\": {\n                \"bool\": {\n                    \"must\": [\n                        {\n                            \"match\": {\n                                \"city\": steps['city-name']\n                            }\n                        },\n                        {\n                            \"match\": {\n                                \"district\": steps['district-name']\n                            }\n                        }\n                    ]\n                }\n            }\n        },\n        'table': 'manager_agent'\n    };\n\n    app.executeFunction('searchQuery', args).then((result) => {\n        if (!result) {\n            args = {\n                steps: steps,\n                agent: {inspection_agent_name:\"Akshey Kumar\", manager_name:\"Delhi backend support\"}\n            };\n            app.executeFunction('preinspectionRequestApi', args).then((result) => {\n                app.sendTextMessage(app.renderMessage('preinspection-success', { data: { leadId: result.LeadID, codeValue: result.SMCodeValue, mobile: result.SMMobileNo } }, `Thank you. Your pre-inspection process is under request. Your lead id. is ` + result.LeadID + `. Our team will contact you for inspection shortly.  Inspection will be done by ${result.SMCodeValue}. Contact number for the inspection agency is ${result.SMMobileNo}`)).then(() => {\n                    app.triggerIntent('anything-else', {});\n                    return;\n                })\n            }).catch(err => {\n                app.log(err, \"ERROR in preinspectionAction\");\n                return resolve();\n            })\n        } else {\n            args = {\n                steps: steps,\n                agent: result\n            }\n            app.executeFunction('preinspectionRequestApi', args).then((result) => {\n                app.sendTextMessage(app.renderMessage('preinspection-success', { data: { leadId: result.LeadID, codeValue: result.SMCodeValue, mobile: result.SMMobileNo } }, `Thank you. Your pre-inspection process is under request. Your lead id. is ` + result.LeadID + `. Our team will contact you for inspection shortly.  Inspection will be done by ${result.SMCodeValue}. Contact number for the inspection agency is ${result.SMMobileNo}`)).then(() => {\n                    app.triggerIntent('anything-else', {});\n                    return;\n                })\n            }).catch(err => {\n                app.log(err, \"ERROR in preinspectionAction\");\n                return resolve();\n            })\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-15T11:44:01.280Z",
          "email": "parvez@yellowmessenger.com",
          "name": "preinspectionAction",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abe0",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    if(app.data.message.length >10){\n        app.pushData({description:app.data.message}, app.context.intent);\n        return resolve();\n    }else{\n        return resolve({\n            success:false,\n            question:app.renderMessage('description-error',{},'')\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.145Z",
          "email": "parvez@yellowmessenger.com",
          "name": "claimDescriptionValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abe1",
          "code": "const errorMessage = () => {\n    app.sendTextMessage(app.renderMessage('error-message', {}, 'There was an error fetching your registered mobile number pelase try again.')).then(() => {\n        app.triggerIntent('default', {});\n        return;\n    })\n}\nfunction redact(mobile) {\n    return mobile.slice(0, 3) + \"****\" + mobile.slice(7, 10)\n}\nreturn new Promise(resolve => {\n    // Your logic goes here\n    try {\n        app.memory.get('userDetails').then(user => {\n            app.log(user, \"User in Mobile qf\");\n            user = JSON.parse(user);\n            let opt = [];\n            if (user.mobile && user.mobile.mobile1 && user.mobile.mobile1 !== \"\" && /^\\d{10}/ig.test(user.mobile.mobile1)) {\n                app.log(redact(user.mobile.mobile1), \"MBILE\")\n                opt.push({\n                    title: redact(user.mobile.mobile1),\n                    text: user.mobile.mobile1\n                });\n                app.log(Object.keys(user.mobile), \"User.Mobile\")\n                if (user.mobile && user.mobile.mobile2 && user.mobile.mobile2 !== \"\" && /^\\d{10}/ig.test(user.mobile.mobile2)) {\n                    opt.push({\n                        title: redact(user.mobile.mobile2),\n                        text: user.mobile.mobile2\n                    });\n                }\n                app.sendQuickReplies({\n                    title: app.renderMessage(\"select-mobile\", {}, \"Please select a mobile number for OTP verification\"),\n                    options: opt\n                }).then(() => {\n                    return resolve();\n                })\n\n            } else {\n                app.sendTextMessage(app.renderMessage('mobile-not-found', {}, '')).then(() => {\n                    app.pushData({ transaction: 'Policy Not found' }, app.context.intent).then(() => {\n                        app.memory.delete('policy_document_lead_id')\n                        app.triggerIntent('anything-else', {});\n                        return;\n                    });\n                })\n            }\n        }).catch(err => {\n            app.log(err, \"ERRORR in MobileQF\");\n            errorMessage();\n        })\n    } catch (err) {\n        app.log(err, \"ERRORR in MobileQF\");\n        errorMessage();\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-25T08:54:50.263Z",
          "email": "parvez@yellowmessenger.com",
          "name": "mobileQF",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abe2",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const to = app.receptionist[args.intentName];//Defined in main function\n    const subject = `API Request Response ${args.type}`;\n    const body = `Request : ${JSON.stringify(args.request)}\\n\n                  Response :  ${JSON.stringify(args.response)}\\n\n                  Error: ${JSON.stringify(args.error)}\\n\n                  Crm Ticket Number: ${args.ticketNumber}`;\n    const sender = \"noreply@yellowmessenger.com\";\n    if (!app.UAT_ENV) {\n        app.sendEmail(to, subject, body, \"\", sender);\n        resolve();\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-12T09:50:27.872Z",
          "email": "parvez@yellowmessenger.com",
          "name": "sendApiFailureEmail",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abe3",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const value = app.data.message;\n    if (/.*(health|travel|car|two wheeler|accident).*$/ig.test(value)) {\n        app.pushData({ \"type\": value }, app.context.intent);\n        return resolve();\n    } else {\n        app.sendQuickReplies({\n            title: app.renderMessage('buy-online-type', {}, \"\"),\n            options: [\n                {\n                    title: \"Health\",\n                    text: \"health\"\n                },\n                {\n                    title: \"Travel\",\n                    text: \"travel\"\n                },\n                {\n                    title: \"Car\",\n                    text: \"car\"\n                },\n                {\n                    title: \"Two Wheeler\",\n                    text: \"two wheeler\"\n                },\n                {\n                    title: \"Accident\",\n                    text: \"accident\"\n                },\n            ]\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.140Z",
          "email": "parvez@yellowmessenger.com",
          "name": "buyOnineTypeValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abe4",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const result = app.data.message.split('$');\n    if (result.length < 2 || result.length > 4) {\n        return resolve({\n            success: false,\n            question: app.renderMessage('city', {}, \"\")\n        })\n    } else {\n        app.setContextParam('city-id', result[1]).then(() => {\n            app.setContextParam('city-name', result[0]).then(() => {\n                app.setContextParam('claim-city',app.data.message);\n                if (app.context.intent === 'claim-intimation') {\n                    app.pushData({ lost_city: result[0] }, app.context.intent);\n                    return resolve();\n                } else {\n                    app.pushData({ CityValue: result[0] }, app.context.intent);\n                    return resolve();\n                }\n            })\n        })\n    }\n});\n",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-09T20:21:20.210Z",
          "email": "parvez@yellowmessenger.com",
          "name": "cityValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abe5",
          "code": "return new Promise(function (resolve) {\n    if (app.term) {\n        app.dataStore.search({\n            table: \"states\",\n            body: {\n                \"query\": {\n                    \"regexp\": { \"state_name\": app.term.toLowerCase() + \".*\" }\n                }\n            }\n        }).then((result) => {\n            resolve(app._.map(result.hits.hits, function (hit) {\n                return [hit._source.state_name, hit._source.state_name+\"$\"+hit._source.state_id];\n            }))\n\n        })\n    } else { resolve([]) }\n})",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.139Z",
          "email": "parvez@yellowmessenger.com",
          "name": "stateAutoComplete",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abe6",
          "code": "const askName = () => {\n    return app.sendTextMessage(app.renderMessage('ask-name',{},'Please tell me your name'));\n}\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    app.memory.get('userDetails').then(user => {\n        user = JSON.parse(user);\n        if (user.name) {\n            app.sendQuickReplies({\n                title: app.renderMessage('ask-name',{},\"Please tell me your name\"),\n                options: [{\n                    title: user.name,\n                    text: user.name\n                }]\n            });\n            return resolve();\n        } else {\n            askName()\n            return resolve();\n        }\n    }).catch(err => {\n        askName()\n        return resolve();\n    })\n\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.140Z",
          "email": "parvez@yellowmessenger.com",
          "name": "garageQF",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abe7",
          "code": "const askName = () => {\n    return app.sendTextMessage(app.renderMessage('policy-number',{},'Please tell me your policy number'));\n}\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    app.memory.get('userDetails').then(user => {\n        user = JSON.parse(user);\n        if (user.policy) {\n            app.sendQuickReplies({\n                title: app.renderMessage('policy-number',{},\"Please tell me your policy number\"),\n                options: [{\n                    title: user.policy,\n                    text: user.policy\n                }]\n            });\n            return resolve();\n        } else {\n            askName()\n            return resolve();\n        }\n    }).catch(err => {\n        askName()\n        return resolve();\n    });\n\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.142Z",
          "email": "parvez@yellowmessenger.com",
          "name": "policyNumberQF",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abe8",
          "code": "const askName = () => {\n    return app.sendTextMessage(app.renderMessage('date-time',{},'Please tell me your name'));\n}\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    app.memory.get('userDetails').then(user => {\n        user = JSON.parse(user);\n        if (user.dateTime) {\n            app.sendQuickReplies({\n                title: app.renderMessage('date-time',{},\"Please tell me your name\"),\n                options: [{\n                    title: user.dateTime,\n                    text: user.dateTime\n                }]\n            });\n            return resolve();\n        } else {\n            askName()\n            return resolve();\n        }\n    }).catch(err => {\n        askName()\n        return resolve();\n    })\n\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.140Z",
          "email": "parvez@yellowmessenger.com",
          "name": "dateAndTimeQF",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abe9",
          "code": "const askName = () => {\n    return app.sendTextMessage(app.renderMessage('ask-name',{},'Please tell me your name'));\n}\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    app.memory.get('userDetails').then(user => {\n        user = JSON.parse(user);\n        if (user.name) {\n            app.sendQuickReplies({\n                title: app.renderMessage('ask-name',{},\"Please tell me your name\"),\n                options: [{\n                    title: user.name,\n                    text: user.name\n                }]\n            });\n            return resolve();\n        } else {\n            askName()\n            return resolve();\n        }\n    }).catch(err => {\n        askName()\n        return resolve();\n    })\n\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.141Z",
          "email": "parvez@yellowmessenger.com",
          "name": "custNameQF",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abea",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const result = app.data.message.split('$');\n    if (result.length < 2 || result.length > 2) {\n        return resolve({\n            success: false,\n            question: app.renderMessage('district', {}, \"\")\n        })\n    } else {\n        app.setContextParam('district-id', result[1]).then(() => {\n            app.memory.set('district_id', result[1]);\n            app.memory.set('districtName', result[0]);\n            app.setContextParam('district-name', result[0]).then(() => {\n                if (app.context.intent === 'claim-intimation') {\n                    app.pushData({ loss_district: result[0] }, app.context.intent);\n                    return resolve();\n                } else {\n                    app.pushData({ DistrictValue: result[0] }, app.context.intent);\n                    return resolve();\n                }\n            })\n        })\n    }\n});\n",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.143Z",
          "email": "parvez@yellowmessenger.com",
          "name": "districtValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abeb",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.executeFunction('claimApi').then(() => {\n        resolve();\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-11T11:14:39.071Z",
          "email": "parvez@yellowmessenger.com",
          "name": "claimAction",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abec",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const steps = app.context.steps;\n    const args = {\n        'es_query': {\n            query: {\n                match: {\n                    \"model_name\": app.data.message.toUpperCase()\n                }\n            }\n        },\n        'table': 'vehicle_model_new'\n    };\n\n    app.log(steps['vehicle-type'], steps['make-id'])\n    if (app.data.message && app.data.message.split('$').length>1) {\n        app.setContextParam('model-name', app.data.message.split('$')[0]).then(() => {\n            app.setContextParam('model-id',app.data.message.split('$')[1] ).then(() => {\n                app.setContextParam('variance', app.data.message.split('$')[2]);\n                app.pushData({ ModelValue: app.data.message}, app.context.intent);\n                return resolve();\n            })\n        })\n    } else {\n        return resolve({\n            success: false,\n            question: app.renderMessage('vehicle-model', {}, \"\")\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-28T08:41:56.844Z",
          "email": "parvez@yellowmessenger.com",
          "name": "vehicleModleValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abed",
          "code": "const askName = () => {\n    return app.sendTextMessage(app.renderMessage('license-no',{},'Please tell me your name'));\n}\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    app.memory.get('userDetails').then(user => {\n        user = JSON.parse(user);\n        if (user.licence) {\n            app.sendQuickReplies({\n                title: app.renderMessage('license-no',{},\"Please tell me your name\"),\n                options: [{\n                    title: user.licence,\n                    text: user.licence\n                }]\n            });\n            return resolve();\n        } else {\n            askName()\n            return resolve();\n        }\n    }).catch(err => {\n        askName()\n        return resolve();\n    })\n\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.144Z",
          "email": "parvez@yellowmessenger.com",
          "name": "licenceNoQF",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abee",
          "code": "const askName = () => {\n    return app.sendQuickReplies({\n        title: app.renderMessage('ask-reg-no', {}, \"Please tell me your name\"),\n        options: [\n            {\n                title: app.renderMessage('reg-no',{},''),\n                text: \"no\"\n            },\n        ]\n    });\n}\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    app.memory.get('userDetails').then(user => {\n        user = JSON.parse(user);\n        if (user.regNo) {\n            app.sendQuickReplies({\n                title: app.renderMessage('ask-reg-no', {}, \"Please tell me your name\"),\n                options: [\n                    {\n                        title: user.regNo,\n                        text: user.regNo\n                    },\n                ]\n            });\n            return resolve();\n        } else {\n            askName()\n            return resolve();\n        }\n    }).catch(err => {\n        askName()\n        return resolve();\n    })\n\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.144Z",
          "email": "parvez@yellowmessenger.com",
          "name": "vechicleRegQF",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abef",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const arry = ['Pvt. Car$6', 'Two-Wheeler$4', 'PCV$7', 'GCV$2', 'Misellaneous Vehicle$10'];\n    if (arry.includes(app.data.message)) {\n        app.setContextParam('vehicle-type', app.data.message);\n        app.memory.set('vehicle_type',app.data.message.split('$')[1]);\n        app.pushData({VehicleTypeValue:app.data.message}, app.context.intent);\n        return resolve();\n    } else {\n        app.sendQuickReplies({\n            title: app.renderMessage('vehicle-type', {}, \"\"),\n            options: [\n                {\n                    title: \"Private Car\",\n                    text: arry[0]\n                },\n                {\n                    title: \"Two Wheeler\",\n                    text: arry[1]\n                },\n                {\n                    title: \"Passenger Carrying Vehicle\",\n                    text: arry[2]\n                },\n                {\n                    title: \"Goods Carrying Vehicle\",\n                    text: arry[3]\n                },\n                {\n                    title: \"Miscellaneous\",\n                    text: arry[4]\n                },\n\n            ]\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.142Z",
          "email": "parvez@yellowmessenger.com",
          "name": "vehicleTypeValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abf0",
          "code": "// const pdfTobyte = (body) => {\n//     return new Promise(resolve => {\n//         let pdfBody = Buffer.from(body, 'base64').toString('utf-8')\n//         let byteNumbers = Array(pdfBody.length);\n//         for (let i = 0; i < pdfBody.length; i++) {\n//             byteNumbers[i] = pdfBody.charCodeAt(i);\n//         }\n//         let byteArray = new Uint8Array(byteNumbers);\n//         return resolve(byteArray);\n//     })\n// }\n// return new Promise(resolve => {\n//     const requestBody = `\n//     <soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:chat=\"http://stub.unotechsoft.com/wsdl/ChatbotService/\" xmlns:com=\"http://stub.unotechsoft.com/wsdl/CommercialVehicleLiteService/\">\n//         <soapenv:Header/>\n//         <soapenv:Body>\n//             <chat:getDocumentList>\n//                 <com:source>TATA-AIG</com:source>\n//                 <com:medium>CHATBOT</com:medium>\n//                 <com:campaign>CHATBOT</com:campaign>\n//                 <com:strServiceToken></com:strServiceToken>\n//                 <chat:PolicyNumber>0157133103</chat:PolicyNumber>\n//                 <chat:GCSource>chat bot</chat:GCSource>\n//                 <chat:DocumentType>Renewal Notice$</chat:DocumentType>\n//             </chat:getDocumentList>\n//         </soapenv:Body>\n//     </soapenv:Envelope>`;\n//     app.requestOptions.body = requestBody;\n//     app.requestOptions.url = app.policyUrl;\n//     app.sendTextMessage('heres')\n//     app.fileRequest(app.requestOptions, function (error, response, body) {\n//         if (error) {\n//             app.sendTextMessage(\"ERROR\\n\" + JSON.stringify(error))\n//         } else if (body) {\n//             body = JSON.parse(app.xmlToJSON.toJson(body));\n//             if (body && body[\"soap:Envelope\"] && body[\"soap:Envelope\"][\"soap:Body\"] && body[\"soap:Envelope\"][\"soap:Body\"][\"ns2:getDocumentListResponse\"] && body[\"soap:Envelope\"][\"soap:Body\"][\"ns2:getDocumentListResponse\"][\"ns2:ChatbotResult\"]) {\n//                 body = JSON.parse(app.xmlToJSON.toJson(body[\"soap:Envelope\"][\"soap:Body\"][\"ns2:getDocumentListResponse\"][\"ns2:ChatbotResult\"]));\n//                 if (body && body['Documents'] && body[\"Documents\"]['Document'] && body[\"Documents\"]['Document']['ByteStream']) {\n//                     body = body[\"Documents\"][\"Document\"][\"ByteStream\"];\n//                     pdfTobyte(body).then((result) => {\n//                         app.uploadFile(result, \"fileName.pdf\").then((fileUrl) => {\n//                             app.sendTextMessage(fileUrl);\n//                             return resolve();\n//                         })\n//                     })\n//                 }\n//             }\n//         }\n//     });\n// })\n\nreturn new Promise(resolve =>{\n\t\tlet curTime = new Date('10/12/2018 04:30 PM');\n\t\tlet lossTime = curTime.toLocaleTimeString().split(':');\n\t\tlossTime = lossTime[0] + \":\" + lossTime[1]\n        app.sendTextMessage(lossTime);\n})",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-11T09:42:48.790Z",
          "email": "parvez@yellowmessenger.com",
          "name": "test",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abf1",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    if(app.data.message.length >6){\n        app.pushData({garage:app.data.message}, app.context.intent);\n        return resolve();\n    }else{\n        return resolve({\n            success:false,\n            question:app.renderMessage('garage-error',{},'')\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-11T08:35:41.906Z",
          "email": "parvez@yellowmessenger.com",
          "name": "garageValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abf2",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    let details = args.details;\n    let policyNo = args.policyNo;\n    let userDetails = JSON.stringify(args.userDetails);\n    try {\n        let renewalDate = new Date(details.renewalDueDate);\n        let currentDate = new Date();\n        if (renewalDate < currentDate || details.premium === '0') {\n            app.sendTextMessage(app.renderMessage(\"renewal-request-output\", {\n                data: {\n                    status: details.renewalStatus,\n                    date: renewalDate.toDateString()\n                }\n            }, `<strong>Your Renewal Status is</strong> : ${details.renewalStatus}\n                            <strong> Due date:</strong> \\n${renewalDate.toDateString()}`)).then(() => {\n                    return resolve(false);\n                });\n        } else {\n            let table = 'renewal_payment_pay_now_links';\n            let searchArgument = {\n                es_query: {\n                    query: {\n                        match: {\n                            \"Policy_No\": policyNo\n                        }\n                    }\n                },\n                table: table\n            };\n            app.executeFunction('searchQuery', searchArgument).then(result => {\n                if (!result) {\n                    app.executeFunction('policyDetails', { 'policyNo': policyNo }).then((customerId) => {\n                        let cards = [];\n                        let transactionId = `${new Date().valueOf()}|${customerId}|${policyNo}|${app.profile.username}`;\n                        let link = `https://bots.botplatform.io/api/tagic/payment?referencenum=T_${transactionId}%amount=${details.premium}%productcode=${details.productCode}%producercode=${details.producerCode}`;\n                        if (app.source === 'facebook') {\n                            let option = {\n                                title: ` Status : ${details.renewalStatus}\\nRenewal due date :${renewalDate.toDateString()} \\nPremium amount : Rs. ${details.premium}`,\n                                options: [\n                                    {\n                                        title: 'Generate Payment Link',\n                                        text: `renewalrequestpaymentlink-$$-${userDetails}-$$-${link}`\n                                    },\n                                    {\n                                        title: 'Pay later',\n                                        text: 'anything else'\n                                    }\n                                ]\n                            };\n                            return resolve(option);\n                        } else {\n                            cards = [{\n                                title: \"Renewal payment\",\n                                text: `          Status : \\n${details.renewalStatus}\n                                         Renewal due date : \\n${renewalDate.toDateString()} \n                                         Premium amount : \\nRs. ${details.premium}`,\n                                actions: [\n                                    {\n                                        title: \"Pay now\",\n                                        text: `renewalrequestpaymentlink-$$-${userDetails}-$$-${link}`\n                                    },\n                                    {\n                                        title: \"Pay later\",\n                                        text: `anything else`\n                                    }\n                                ]\n                            }];\n                            return resolve(cards)\n                        }\n                    })\n                } else {\n                    if (app.source === 'facebook') {\n                        let option = {\n                            title: ` Status : ${details.renewalStatus}\\nRenewal due date :${renewalDate.toDateString()} \\nPremium amount : Rs. ${details.premium}`,\n                            options: [\n                                {\n                                    title: 'Generate Payment Link',\n                                    text: `renewalrequestpaymentlink-$$-${userDetails}-$$-${result.Pay_Now_Link.replace(/&/g, '%')}`\n                                },\n                                {\n                                    title: 'Pay later',\n                                    text: 'anything else'\n                                }\n                            ]\n                        };\n                        return resolve(option);\n                    } else {\n                        cards = [{\n                            title: \"Renewal payment\",\n                            text: `          Status : \\n${details.renewalStatus}\n                                         Renewal due date : \\n${renewalDate.toDateString()} \n                                         Premium amount : \\nRs. ${details.premium}`,\n                            actions: [\n                                {\n                                    title: \"Pay now\",\n                                    text: `renewalrequestpaymentlink-$$-${userDetails}-$$-${result.Pay_Now_Link.replace(/&/g, '%')}`\n                                },\n                                {\n                                    title: \"Pay later\",\n                                    text: `anything else`\n                                }\n                            ]\n                        }];\n                        return resolve(cards);\n                    }\n                }\n            })\n        }\n    } catch (err) {\n        app.log(err, \"ERROR\");\n        app.sendTextMessage('ERROR');\n        resolve(false);\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-31T17:52:50.339Z",
          "email": "parvez@yellowmessenger.com",
          "name": "getPaymentLink",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abf3",
          "code": "\nreturn new Promise(resolve => {\n    // Your logic goes here\n    if(app.prediction.global_model.intent === 'yes' && app.prediction.global_model.confidence > 0.85){\n        app.pushData({tie_up_garages:\"yes\"},app.context.intent);\n        return resolve();\n    }else{\n        app.pushData({tie_up_garages:\"no\"},app.context.intent);\n        return resolve();\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.145Z",
          "email": "parvez@yellowmessenger.com",
          "name": "tieupGaragesValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abf4",
          "code": "const claimTableName = \"claim_intimation_lead_id\";\nconst errorMessage = (data, requestBody, responseBody, error, steps, elapsedTime) => {\n\tdata.leadId = data.leadId ? data.leadId : \"API Timed Out or Error\";\n\tdata.assignedTo = 'dgavali';\n\tapp.executeFunction('crmApi', args = { data: data, status: 'Open', intentName: \"claim-intimation\" }).then((ticket) => {\n\t\tapp.pushData({ transaction: 'Failed', message: data.leadId, crm_ticket: ticket }, app.context.intent).then(() => {\n\t\t\tapp.memory.delete(claimTableName);\n\t\t});\n\t\tapp.sendTextMessage(app.renderMessage('claim-error-success', { ticket: ticket }, \"\")).then(() => {\n\t\t\tapp.executeFunction('apiResponseDatabase', args = { request: requestBody, response: responseBody, error: error, tableName: \"claim_intimation_api_database\", \"type\": \"Claim Intimation\", \"elapsedTime\": elapsedTime, steps: steps });\n\t\t\tapp.executeFunction('sendApiFailureEmail', args = { request: requestBody, response: responseBody, error: error, tableName: \"claim_intimation_api_database\", \"type\": \"Claim Intimation\", \"elapsedTime\": elapsedTime, \"ticketNumber\": ticket, \"intentName\": 'claim-intimation' })\n\t\t\tapp.triggerIntent('anything-else', {});\n\t\t\treturn;\n\t\t});\n\t});\n\n}\n\nconst successErrorMessage = (data, requestBody, responseBody, error, steps, elapsedTime, status) => {\n\treturn new Promise(resolve => {\n\t\tapp.executeFunction('apiResponseDatabase', args = { request: requestBody, response: responseBody, error: error, tableName: \"claim_intimation_api_database\", \"type\": \"Claim Intimation\", \"elapsedTime\": elapsedTime })\n\t\tapp.executeFunction('crmApi', args = { data: data, status: status, intentName: \"claim-intimation\" }).then((ticketNumber) => {\n\t\t\tapp.pushData({ transaction: 'success', message: data.leadId ? data.leadId : data.claimNo, crm_ticket: ticketNumber }, app.context.intent).then(() => {\n\t\t\t\tapp.sendTextMessage(app.renderMessage(\"ticket-number\", { ticket: ticketNumber }, \"\")).then(() => {\n\t\t\t\t\tapp.memory.delete(claimTableName);\n\t\t\t\t\tapp.triggerIntent('anything-else', {});\n\t\t\t\t\treturn;\n\t\t\t\t})\n\t\t\t})\n\t\t})\n\t});\n}\n\nreturn new Promise(resolve => {\n\tif (app.UAT_ENV) {\n\t\tapp.executeFunction('newClaim').then(() => {\n\t\t\treturn resolve();\n\t\t})\n\t} else {\n\t\ttry {\n\t\t\tconst steps = app.context.steps;\n\t\t\t// app.sendTextMessage(JSON.stringify(steps));\n\t\t\tlet source = 'TATA-AIG';\n\t\t\tlet medium = 'CHATBOT';\n\t\t\tlet email = steps['email'] === 'noemailid' ? \"\" : steps['email'];\n\t\t\tlet lossTime = new Date(steps['accident-date-time']).toLocaleTimeString().split(':');\n\t\t\tlossTime = lossTime[0] + \":\" + lossTime[1]\n\t\t\tlet lossDate = steps['date-time'].split(' ')[0];\n\t\t\tlet curDate = new Date().toLocaleDateString().split('-');\n\t\t\tcurDate = `${curDate[2]}/${curDate[1]}/${curDate[0]}`\n\t\t\tlet curTime = new Date();\n\t\t\tcurTime = new Date(curTime.getTime() + 330 * 60000).toLocaleTimeString().split(':');\n\t\t\tcurTime = curTime[0] + \":\" + curTime[1];\n\t\t\tlet insuredMobile = steps['insured-person'] === 'yes' ? steps['mobile'] : steps['insured-mobile'];\n\t\t\tlet pincode = steps['claim-city'].split('$')[3];\n\t\t\tlet settlingOffice = steps['claim-city'].split('$')[1];\n\t\t\tlet curCity = steps['city-name'] ? steps['city-name'] : \"\";\n\t\t\tlet garage = steps['garage-or-not'] === 'With Insured' ? curCity + ', ' + steps['garage-or-not'] : steps['garage-or-not'];\n\t\t\tlet lossLocation = `${curCity}, ${steps['district-name'] ? steps['district-name'] : \"\"}, ${steps['state-name'] ? steps['state-name'] : \"\"}`;\n\t\t\tif (app.UAT_ENV) {\n\t\t\t\tsource = 0;\n\t\t\t\tmedium = 0;\n\t\t\t}\n\t\t\t//If location is garage or other\n\t\t\tif (steps['garage-or-not'] === 'garage') {\n\t\t\t\tgarage = `${steps.garage}, ${steps['cur-city-name']}, ${steps['cur-district-name']}, ${steps['cur-state-name']}`;\n\t\t\t} else if (steps['garage-or-not'] === 'With Insured') {\n\t\t\t\tgarage = `${steps['cur-landmark']}, ${steps['cur-city-name']}, ${steps['cur-district-name']}, ${steps['cur-state-name']}`;\n\t\t\t}\n\t\t\tlet userData = {\n\t\t\t\tusername: steps['customer-name'],\n\t\t\t\tmobileNo: steps['mobile'],\n\t\t\t\temail: email,\n\t\t\t\tpolicyNo: steps['policy-number'],\n\t\t\t\tleadId: \"\",\n\t\t\t\tclaimNo: \"\",\n\t\t\t\tcallerRelation: steps['insured']\n\t\t\t}\n\t\t\tlet claimType = { \"OD\": \"24971\", \"stolen\": \"9948\", \"parked\": \"24971\", \"Key\": \"24873\", \"tyre\": \"24879\" };\n\n\t\t\t//API BODY \n\t\t\tlet options = {\n\t\t\t\tmethod: 'POST',\n\t\t\t\turl: app.claimUrl,\n\t\t\t\tqs: { wsdl: '' },\n\t\t\t\theaders:\n\t\t\t\t{\n\t\t\t\t\t'Postman-Token': 'e902a49d-0b14-4212-9140-f9aefd9a6fc2',\n\t\t\t\t\t'cache-control': 'no-cache',\n\t\t\t\t\t'Content-Type': 'text/xml'\n\t\t\t\t},\n\t\t\t\tbody: `\n               \n<soapenv:Envelope\n\txmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\"\n\txmlns:mot=\"http://stub.unotechsoft.com/wsdl/MotorClaimService/\"\n\txmlns:cla=\"http://schemas.datacontract.org/2004/07/ClaimEntities\"\n\txmlns:arr=\"http://schemas.microsoft.com/2003/10/Serialization/Arrays\">\\n    \n\t<soapenv:Header />\\n    \n\t<soapenv:Body>\\n        \n\t\t<mot:claimServiceRegisterClaim>\\n            \n\t\t\t<mot:source>${source}</mot:source>\\n            \n\t\t\t<mot:medium>${medium}</mot:medium>\\n            \n\t\t\t<mot:campaign>${medium}</mot:campaign>\\n            \n\t\t\t<mot:strServiceToken/>\\n            \n\t\t\t<mot:PolicyNumber>${steps['policy-number']}</mot:PolicyNumber>\\n            \n\t\t\t<mot:LossDate>${lossDate}</mot:LossDate>\\n            \n\t\t\t<mot:IntDate>${curDate}</mot:IntDate>\\n            \n\t\t\t<mot:LossTime>${lossTime}</mot:LossTime>\\n            \n\t\t\t<mot:IntTime>${curTime}</mot:IntTime>\\n            \n\t\t\t<mot:NOLCode>${claimType[steps['claim-type']]}</mot:NOLCode>\\n            \n\t\t\t<mot:LossDescCode>999</mot:LossDescCode>\\n            \n\t\t\t<mot:LossDesc>${steps['description']}</mot:LossDesc>\\n            \n\t\t\t<mot:PinCode>${pincode}</mot:PinCode>\\n            \n\t\t\t<mot:ContactNo>${insuredMobile}</mot:ContactNo>\\n            \n\t\t\t<mot:IsClaimantInsured>Yes</mot:IsClaimantInsured>\\n            \n\t\t\t<mot:DriverName>${steps['driver-name']}</mot:DriverName>\\n            \n\t\t\t<mot:LicenseNo>${steps['license-no']}</mot:LicenseNo>\\n            \n\t\t\t<!--Optional:-->\\n            \n\t\t\t<mot:SettlingOffice>${settlingOffice.toUpperCase()}</mot:SettlingOffice>\\n            \n\t\t\t<!--Optional:-->\\n            \n\t\t\t<mot:ClaimType>${steps['claim-type']}</mot:ClaimType>\\n            \n\t\t\t<mot:EmailID>${email}</mot:EmailID>\\n            \n\t\t\t<mot:CallerName>${steps['cust-name']}</mot:CallerName>\\n            \n\t\t\t<mot:CallerContactNo>${insuredMobile}</mot:CallerContactNo>\\n            \n\t\t\t<mot:GarageDetails>${garage}</mot:GarageDetails>\\n            \n\t\t\t<mot:Landmark>${steps['loss-landmark']}</mot:Landmark>\\n            \n\t\t\t<mot:AddOfAccident>${lossLocation}</mot:AddOfAccident>\\n            \n\t\t\t<mot:SARMLRNo />\\n            \n\t\t\t<mot:AddInfo />\\n            \n\t\t\t<mot:CertNo />\\n            \n\t\t\t<mot:CauseOfLossCode>${claimType[steps['claim-type']]}</mot:CauseOfLossCode>\\n            \n\t\t\t<!--Optional:-->\\n            \n\t\t\t<mot:ClaimStatus>Open</mot:ClaimStatus>\\n            \n\t\t\t<!--Optional:-->\\n            \n\t\t\t<mot:AnatCode />\\n            \n\t\t\t<!--Optional:-->\\n            \n\t\t\t<mot:InjuryCode />\\n            \n\t\t\t<!--Optional:-->\\n            \n\t\t\t<mot:lstIndianCurrencyRiskDetails>\\n                \n\t\t\t\t<!--Zero or more repetitions:-->\\n                \n\t\t\t\t<cla:GDtRiskDetails_INR>\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:RowIndex />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:ACCOUNT_LINE />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:Claimable_Amount />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:MemberID />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:NUM_LOCATION_CD />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:Num_Assessed_Amount />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:Num_Balance_SI />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:Num_Claim_Amount />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:Num_Cover_Code />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:Num_Cubic_Capacity />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:Num_SI />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:Num_Serial />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:Num_Voluntary_Excess />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:Policy_Risk_Serial />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:Risk_Detail_Serial />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:STATUS />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:Txt_Cover_Code />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:Txt_Risk_Element />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:Txt_Risk_Element_Type />\\n                    \n\t\t\t\t\t<!--Optional:-->\\n                    \n\t\t\t\t\t<cla:UniqueCode />\\n                \n\t\t\t\t</cla:GDtRiskDetails_INR>\\n            \n\t\t\t</mot:lstIndianCurrencyRiskDetails>\\n            \n\t\t\t<!--Optional:-->\\n            \n\t\t\t<mot:dicLVWFParams>\\n                \n\t\t\t\t<!--Zero or more repetitions:-->\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>KeyDms</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>192.168.140.97:8080/dms.TAGIC/initiatelogin.do?</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>SLPageName</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>ScrClm_ClaimRegistration</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>ConfiguratorUrl</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>http://localhost/Configurator</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>CURRENT_STATE</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>START_REGISTRATION</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>OTHER_STATE_INFO</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value />\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>WORKFLOW_NAME</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>MotorODWorkflow</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>LOB</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>D000020</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>PROCESS_NAME</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>35</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>GUID_WORKFLOW</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>6a7140e4-c910-44c1-8cae-f55ae9166d72</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>LINK_ID</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>0</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>SIU</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value />\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>KYC</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>KYC</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>AML</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>Y</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>APPROVALSTATUS</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>0</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>CURRENT_OUTSTANDING</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>1</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>ISCLAIMCANCELLED</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>N</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>ISCLAIMClOSED</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>N</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>AppUserID</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>1003</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>UserRole</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>ADMIN</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>AppSessionID</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>SL-CONF-100000000432188</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>SessionIDDMS</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>100000000432188</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>SystemMailSender</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>abcinsuranceonline@gmail.com</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>SessionIsNothing</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>False</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>ErrorLogCheck</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>0</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n                \n\t\t\t\t<arr:KeyValueOfstringstring>\\n                    \n\t\t\t\t\t<arr:Key>AssemblyVersionCheck</arr:Key>\\n                    \n\t\t\t\t\t<arr:Value>0</arr:Value>\\n                \n\t\t\t\t</arr:KeyValueOfstringstring>\\n            \n\t\t\t</mot:dicLVWFParams>\\n        \n\t\t</mot:claimServiceRegisterClaim>\\n    \n\t</soapenv:Body>\\n\n</soapenv:Envelope>\n\n        `\n\t\t\t};\n\t\t\tconst startTime = new Date();\n\t\t\tapp.sendTextMessage('Please wait while I register your claim, It may take some time...').then(() => {\n\t\t\t\tapp.request.request(options, function (err, response, body) {\n\t\t\t\t\tapp.executeFunction('apiResponseDatabase', args = { request: options, response: response, error: err, tableName: \"claim_api\", \"type\": steps['policy-number'] });\n\t\t\t\t\tapp.elapsedTime(startTime).then((elapsedTime) => {\n\t\t\t\t\t\tif (err || response.statusCode !== 200) {\n\t\t\t\t\t\t\terrorMessage(userData, options, response, err, steps, elapsedTime);\n\t\t\t\t\t\t\treturn resolve();\n\t\t\t\t\t\t} else {\n\t\t\t\t\t\t\tlet result = JSON.parse(app.xmlToJSON.toJson(body));\n\t\t\t\t\t\t\tif (result['soap:Envelope']['soap:Body']['claimServiceRegisterClaimResponse']['ClaimServiceRegisterClaimResult']) {\n\t\t\t\t\t\t\t\tconst details = result['soap:Envelope']['soap:Body']['claimServiceRegisterClaimResponse']['ClaimServiceRegisterClaimResult'];\n\t\t\t\t\t\t\t\tif ((details && details[\"ns2:Message\"] && details[\"ns2:Message\"][\"ns2:MessageType\"] && details[\"ns2:Message\"][\"ns2:MessageType\"] == \"ERROR\") ||\n\t\t\t\t\t\t\t\t\t(details && details[\"ns2:Message\"] && details[\"ns2:Message\"]['ns2:Message'] && details[\"ns2:Message\"]['ns2:Message'] === \"Problem in Selecting Risk Details\")) {\n\t\t\t\t\t\t\t\t\tif (details[\"ns2:Message\"][\"ns2:Message\"] && details[\"ns2:Message\"][\"ns2:Message\"] !== 'Problem in Selecting Risk Details') {\n\t\t\t\t\t\t\t\t\t\tapp.sendTextMessage(details[\"ns2:Message\"][\"ns2:Message\"]).then(function () {\n\t\t\t\t\t\t\t\t\t\t\t//Conversation is finshed but CRM ticket is open\n\t\t\t\t\t\t\t\t\t\t\tuserData.leadId = details[\"ns2:Message\"][\"ns2:Message\"]\n\t\t\t\t\t\t\t\t\t\t\terrorMessage(userData, options, response, err, steps, elapsedTime).then(() => {\n\t\t\t\t\t\t\t\t\t\t\t\treturn resolve()\n\t\t\t\t\t\t\t\t\t\t\t})\n\t\t\t\t\t\t\t\t\t\t});\n\t\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\t\telse {\n\t\t\t\t\t\t\t\t\t\terrorMessage(userData, options, response, err, steps, elapsedTime);\n\t\t\t\t\t\t\t\t\t\treturn resolve();\n\t\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\t} else if (details['ns2:ClaimDetails'] && details['ns2:ClaimDetails']['ns2:GDTClaimDetails']['ns2:ClaimNo'] && details['ns2:ClaimDetails']['ns2:GDTClaimDetails']['ns2:ClaimNo'].trim() && JSON.stringify(details['ns2:ClaimDetails']['ns2:GDTClaimDetails']['ns2:ClaimNo']) != \"\") {\n\t\t\t\t\t\t\t\t\tlet claim_no = details['ns2:ClaimDetails']['ns2:GDTClaimDetails']['ns2:ClaimNo'].toString();\n\t\t\t\t\t\t\t\t\tuserData.claimNo = details['ns2:ClaimDetails']['ns2:GDTClaimDetails']['ns2:ClaimNo'];\n\t\t\t\t\t\t\t\t\tapp.sendTextMessage(app.renderMessage('claim-thankyou', { details: { claim: claim_no } }, `Thank you. We have taken your claim request. Your claim number is <strong>${claim_no}</strong>.`)).then(() => {\n\t\t\t\t\t\t\t\t\t\tapp.sendTextMessage(app.renderMessage('claim-documents', {}, `Our Claim officials will contact you within the next 48 workings hours. Request you to kindly submit the following documents (self-attested) during the survey:\n                                                    1. Claim form\n                                                    2. Driving license copy\n                                                    3. RC copy\n                                                    4. FIR copy (if any)\n\n                                                P.S- Additional Documents maybe asked for, as per the merit of your claim. It will be informed to you by our claim officials.`));\n\t\t\t\t\t\t\t\t\t}).then(function () {\n\t\t\t\t\t\t\t\t\t\tlet status = steps['motor-type'] === 'c2' ? \"Open\" : \"Closed\";\n\t\t\t\t\t\t\t\t\t\tsuccessErrorMessage(userData, options, response, err, steps, elapsedTime, status).then(() => {\n\t\t\t\t\t\t\t\t\t\t\treturn;\n\t\t\t\t\t\t\t\t\t\t})\n\t\t\t\t\t\t\t\t\t});\n\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t} else {\n\t\t\t\t\t\t\t\terrorMessage(userData, options, response, err, steps, elapsedTime);\n\t\t\t\t\t\t\t\treturn resolve();\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t\t});\n\t\t\t\t});\n\t\t\t});\n\t\t} catch (err) {\n\t\t\tapp.log(err, \"THIS IS ERROR\");\n\t\t\terrorMessage(userData, requestBody, '', err, '', '');\n\t\t\treturn resolve();\n\t\t}\n\t}\n})",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-02T11:48:45.684Z",
          "email": "parvez@yellowmessenger.com",
          "name": "claimApi",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abf5",
          "code": "return new Promise(function (resolve) {\n    if (app.term) {\n        app.dataStore.search({\n            table: \"vehicle_make\",\n            body: {\n                \"query\": {\n                    \"regexp\": { \"make_name\": app.term.toLowerCase() + \".*\" }\n                }\n            }\n        }).then((result) => {\n                    app.log('here')\n\n            resolve(app._.map(result.hits.hits, function (hit) {\n                return [hit._source.make_name, hit._source.make_name+\"$\"+hit._source.make_id];\n            }))\n\n        })\n    } else { resolve([]) }\n})",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-28T11:49:43.758Z",
          "email": "parvez@yellowmessenger.com",
          "name": "vehicleMakeAutoComplete",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abf6",
          "code": "// Your code goes here\nlet toTitleCase = (str) => {\n    return str.replace(/\\w\\S*/gi, function (txt) { return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase(); });\n}\nconst callAgent = (userName, userPhone, userEmail, policyNo, language) => {\n    return new Promise(resolve => {\n        let issueString = \"Phone : \" + userPhone;\n        app.sendTextMessage(app.renderMessage('agent-wait', {}, \"Please wait while I contact my support center...\")).then(() => {\n            app.raiseTicket({\n                issue: issueString,\n                contact: {\n                    phone: userPhone,\n                    name: userName,\n                    email: userEmail\n                },\n                priority: 'MEDIUM',\n                manualAssignment: true,\n                category: 'others'\n            }).then(function (ticketData) {\n                if (ticketData && ticketData.assignedTo) {\n                    app.log(ticketData, \"Ticket data\");\n                    // app.memory.set('othersUserData', {\n                    const data = {\n                        username: userName,\n                        email: userEmail,\n                        mobileNo: userPhone,\n                        leadId: 'Communicated in ' + (language === 'en' ? 'English' : 'Hindi'),\n                        policyNo: policyNo,\n                        assignedTo: ticketData.assignedTo,\n                    }\n                    app.sendTextMessage(app.renderMessage('support-team', { agent: \"\" }, \"Our customer support team will assist you shortly...\")).then(() => {\n                        app.pushData({ transaction: 'success', assign_to: data.assignedTo, link: app.getSessionMessageLogUrl() }, app.context.intent).then(() => {\n                            app.pauseBot();\n                            return resolve();\n                        })\n                    })\n                    // app.sendTextMessage(\"Our agent will assist you. Please wait while we connect you to our agent.\");\n                } else {\n                    app.sendTextMessage(app.renderMessage('agents-not-available', {}, '')).then(() => {\n                        const data = {\n                            username: userName,\n                            email: userEmail,\n                            mobileNo: userPhone,\n                            leadId: (language === 'en' ? 'English' : 'Hindi'),\n                            policyNo: policyNo,\n                            assignedTo: 'ois_raviuda'\n                        };\n                        // app.executeFunction('crmApi', args = { data: data, status: 'Open', intentName: \"others\" });\n                        app.pushData({ 'assign_to': \"Agent was offline\", transaction: \"Failed\", link: app.getSessionMessageLogUrl() }, app.context.intent).then(() => {\n                            app.options.targetLanguage = 'en';\n                            app.memory.delete('others_lead_id');\n                            app.memory.delete('othersLanguage');\n                            app.memory.delete('support_lead_id');\n                            app.options.targetLanguage = 'en';\n                            app.triggerIntent('anything-else', {});\n                            return;\n                        })\n\n                    })\n                }\n            });\n        });\n    })\n}\n\nreturn new Promise((resolve, reject) => {\n    app.memory.get('userDetails').then((result) => {\n        let userDetials = JSON.parse(result);\n        app.log(userDetials, \"UserDetails in connect agent\");\n        callAgent(userDetials.name, userDetials.agentMobile, userDetials.email, app.context.steps['policy-number'], app.context.steps['select-language']).then(() => {\n            return resolve();\n        })\n    }).catch(err => {\n        app.log(err, \"ERROR in connect agent\");\n        callAgent('', '', '').then(() => {\n            return resolve();\n        })\n    });\n})",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-25T11:03:07.788Z",
          "email": "parvez@yellowmessenger.com",
          "name": "connectToAgent",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abf7",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const result = app.data.message.split('$');\n    if (result.length < 2 || result.length > 2) {\n        return resolve({\n            success: false,\n            question: app.renderMessage('state', {}, \"\")\n        })\n    } else {\n        app.setContextParam('cur-state-id', result[1]).then(() => {\n            app.memory.set('state_id', result[1]);\n            app.setContextParam('cur-state-name', result[0]).then(() => {\n                if (app.context.intent === 'claim-intimation') {\n                    app.pushData({ cur_state: result[0] }, app.context.intent);\n                    return resolve();\n                } else {\n                    app.pushData({ StateValue: result[0] }, app.context.intent);\n                    return resolve();\n                }\n            })\n        })\n    }\n});\n",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-11T11:38:23.423Z",
          "email": "parvez@yellowmessenger.com",
          "name": "claimCurrentStateValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abf8",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const array = ['claim-intimation','preinspection-status','buy-online', 'others', 'general-query', 'tie-up-locations', 'customer-care']\n    app.validate(app.data.message).then((result) => {\n        if (!result) {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"phone-validator\", {}, \"Please enter a valid 10 digit mobile number\")\n            })\n        } else if (/^[6,7,8,9]\\d{9}$/ig.test(result)) {\n            result = result.toLowerCase();\n            app.setContextParam('agent-mobile', result);\n            let dataToPUsh ={ ProposerAgentMobile: result }\n            if(app.context.intent === 'renewal-request-payment'){\n                dataToPUsh = { mobile_number: result };\n            }else if(array.includes(app.context.intent)){\n                dataToPUsh = {mobile:result};\n            }\n            app.pushData(dataToPUsh, app.context.intent)\n            app.executeFunction('updateCustomerInformation', args = { field: \"agentMobile\", value: result });\n            return resolve();\n        } else {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"phone-validator\", {}, \"Please enter a valid 10 digit mobile number\")\n            })\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-22T08:58:16.296Z",
          "email": "parvez@yellowmessenger.com",
          "name": "agentMobileValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abf9",
          "code": "const errorMessage = (requestBody, responseBody, error, elapsedTime) => {\n    app.pushData({ transaction: 'Failed' }, app.context.intent);\n    app.executeFunction('apiResponseDatabase', args = { request: requestBody, response: responseBody, error: error, tableName: \"preinspection_api_database\", \"type\": \"Lead Status\", \"elapsedTime\": elapsedTime })\n    return app.sendTextMessage(app.renderMessage('preinspection-error', {}, \"There was some error while processing your preinspection request. Pelase try again.\")).then(() => {\n        app.memory.delete('preinspection_status_lead_id');\n        app.clearContext();\n        app.data.message = 'help';\n        return app.start();\n    })\n};\nreturn new Promise(resolve => {\n    // Your logic goes here\n    const reqParams = { LeadNo: app.context.steps['lead-number'], RegNo: '', AgencyId: '1' };\n    app.preinspectionRequest.url = app.preinspectionRequest.url + 'GetLead';\n    app.preinspectionRequest.body = reqParams;\n    const startTime = new Date();\n    app.log(app.preinspectionRequest, \"REQUEST BODY\")\n    app.request.request(app.preinspectionRequest, function (err, response, body) {\n        app.log(body, \"Preinspection response body\")\n        app.elapsedTime(startTime).then((elapsedTime) => {\n            if (err || response.statusCode != 200) {\n                errorMessage(app.preinspectionRequest, response, err, elapsedTime);\n                app.log(response, \"ERROR\")\n                app.sendTextMessage('error')\n            } else {\n                app.executeFunction('apiResponseDatabase', args = { request: app.preinspectionRequest, response: body, error: err, tableName: \"preinspection_api_database\", \"type\": \"Lead Status\", \"elapsedTime\": elapsedTime });\n                app.sendTextMessage(app.renderMessage(\"status-success\", { data: { QCStatus: body[0].QCStatus, SMName: body[0].SMCode, SMNumber: body[0].SMContact_No } }, \"Thank you. I found the below report on your preinspection status:\\n\" + \"<strong>Quality Check Status:</strong> \" + body[0].QCStatus + \"\\n<strong>Inspection Agency:</strong>\" + body[0].SMCode.split(\"-\")[0].trim() + \"\\n<strong>Inspection Agency contact number:</strong>\" + body[0].SMCode.split(\"-\")[1].trim())).then(() => {\n                    app.pushData({ transaction: 'Success' }, app.context.intent).then(() => {\n                        app.memory.delete('preinspection_status_lead_id');\n                        app.triggerIntent('anything-else', {});\n                        return;\n                    })\n                })\n            }\n        })\n    });\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-10T15:08:10.833Z",
          "email": "parvez@yellowmessenger.com",
          "name": "preinspectionStatusAction",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abfa",
          "code": "\nreturn new Promise(resolve => {\n    // Your logic goes here\n    if(app.prediction.global_model.intent === 'yes' && app.prediction.global_model.confidence > 0.85){\n        app.pushData({death_injury:\"yes\"},app.context.intent);\n        return resolve();\n    }else{\n        app.pushData({death_injury:\"no\"},app.context.intent);\n        return resolve();\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-05T05:13:04.460Z",
          "email": "parvez@yellowmessenger.com",
          "name": "deathInjuryValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abfb",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    if (app.data && app.data.message) {\n        app.validate(app.data.message).then((result) => {\n            if (!result && app.context.intent != 'calim-intimation') {\n                return resolve({\n                    success: false,\n                    question: app.renderMessage(\"email-validator\", {}, \"Please enter a valid email id\")\n                })\n            } else if (/^(([^<>()\\[\\]\\\\.,;:\\s@\"]+(\\.[^<>()\\[\\]\\\\.,;:\\s@\"]+)*)|(\".+\"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,}))$/g.test(result)) {\n                result = result.toLowerCase();\n                app.setContextParam('email-id', result);\n                app.pushData({ email: result }, app.context.intent)\n                app.executeFunction('updateCustomerInformation', args = { field: \"email\", value: result });\n                return resolve();\n            } else if (result.toLowerCase() === 'noemailid') {\n                app.setContextParam('email', \"\");\n                return resolve();\n            } else {\n                return resolve({\n                    success: false,\n                    question: app.renderMessage(\"email-validator\", {}, \"Please enter a valid email id\")\n                })\n            }\n        })\n    } else {\n        return resolve({\n            success: false,\n            question: app.renderMessage(\"email-validator\", {}, \"Please enter a valid email id\")\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-09T18:46:10.407Z",
          "email": "parvez@yellowmessenger.com",
          "name": "emailValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abfc",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.validate(app.data.message).then((result) => {\n        if (!result) {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"insured-name\", {}, \"Please tell me your name\")\n            })\n        } else {\n            app.setContextParam('insured-name', result);\n            let data = { CustomerName: result }\n            if(app.context.intent === 'claim-intimation'){\n                data = {insured_person:result}\n            }\n            app.pushData(data, app.context.intent);\n            return resolve();\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.143Z",
          "email": "parvez@yellowmessenger.com",
          "name": "insuredNameValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abfd",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.validate(app.data.message).then((result) => {\n        if (!result) {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"phone-validator\", {}, \"Please enter a valid 10 digit mobile number\")\n            })\n        } else if (/^[6,7,8,9]\\d{9}$/ig.test(result)) {\n            result = result.toLowerCase();\n            app.setContextParam('agent-mobile', result);\n            let dataToPUsh ={ insured_mobile: result }\n            if(app.context.intent === 'renewal-request-payment'){\n                dataToPUsh = { mobile_number: result };\n            }\n            app.pushData(dataToPUsh, app.context.intent)\n            app.executeFunction('updateCustomerInformation', args = { field: \"insured_mobile\", value: result });\n            return resolve();\n        } else {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"phone-validator\", {}, \"Please enter a valid 10 digit mobile number\")\n            })\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-11-23T06:10:41.144Z",
          "email": "parvez@yellowmessenger.com",
          "name": "insuredMobile",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abfe",
          "code": "//Product code for preinspection request 3121 is for 4 wheeler and 3122 is for 2 wheeler\nconst agentNameMapping = {\n    'jaymewadatataaigcom': \"Jmewada\",\n    'krishmamehtatataaigcom': \"krmehta2\",\n    'shivampandeytataaigcom': \"spandey10\",\n    'santoshk': \"Skanoji\",\n    'rucha': \"rukolte\",\n    'ois_raviuda': 'ois_raviuda'\n};\n\nif (args.intentName === 'others' || args.intentName === 'customer-care') {\n    args.data.assignedTo = agentNameMapping[args.data.assignedTo];\n}\n\nreturn new Promise(resolve => {\n    let product = \"\";\n    let productCategory = \"\";\n    if (app.UAT_ENV) {\n        product = args.data.product ? args.data.product : \"\";\n        productCategory = args.intentName === 'preinspection-request' ? \"1\" : \"\";\n        productCategory = args.data.productCategory ? args.data.productCategory : productCategory;\n    }\n    try {\n        let body = {\n            \"system_name\": \"Chat Bot\",\n            \"user_name\": app.crmUser,\n            \"authkey\": app.crmAuth,\n            \"channel\": \"webcht127\",\n            \"ticketData\": {\n                \"queue\": app.codeType[args.intentName][0].toString(),\n                \"sr\": app.codeType[args.intentName][1].toString(),\n                \"sub_sr\": app.codeType[args.intentName][2].toString(),\n                \"priority\": \"P1\",\n                \"product\": product,\n                \"product_category\": productCategory,\n                \"caller_name\": args.data.username ? args.data.username : \"\",\n                \"caller_mobile_number\": args.data.mobileNo,\n                \"caller_relation\": args.data.callerRelation ? args.data.callerRelation.toLowerCase() : \"insured\",\n                \"servicing_branch\": \"\",\n                \"contact_status\": \"\",\n                \"cancellation_reason\": \"\",\n                \"branch_code\": \"85\",\n                \"remarks\": args.data.leadId ? args.data.leadId : \"\",\n                \"work_note\": app.getSessionMessageLogUrl(),\n                \"claim_no\": args.data.claimNo ? args.data.claimNo : \"\",\n                \"claim_settling_office\": \"\",\n                \"assigned_user_name\": args.status === 'Closed' ? \"Pbharga\" : args.data.assignedTo ? args.data.assignedTo : \"ois_raviuda\",\n                \"service_status\": args.status\n            },\n            \"customerData\": {\n                \"customer_id\": \"\",\n                \"customer_name\": args.data.username ? args.data.username : \"\",\n                \"customer_email\": args.data.email,\n                \"customer_phone\": args.data.mobileNo,\n                \"customer_policy_number\": args.data.policyNo ? args.data.policyNo : \"\",\n                \"pan_number\": \"\",\n                \"passport_number\": \"\",\n                \"aadhar\": \"\",\n                \"customer_city\": \"\"\n            },\n        }\n        console.log(body, \"body in crm\");\n        let option = {\n            url: app.crmUrl,\n            method: 'POST',\n            timeout: app.timeOut,\n            body: JSON.stringify(body),\n            headers: {\n                'Content-Type': 'application/json'\n            }\n        }\n        app.log(option, \"THis is option\")\n        app.request.request(option, (err, res, body) => {\n            let apiDatabaseArgs = {\n                tableName: 'crm',\n                request: option,\n                response: body,\n                error: err,\n                type: args.intentName\n            };\n            if (err) {\n                app.log(err, \"ERROR in CRM\");\n                app.executeFunction(\"apiResponseDatabase\", apiDatabaseArgs);\n                return resolve();\n\n            } else {\n                body = JSON.parse(body);\n                app.log(body, \"Result of CMR\");\n                apiDatabaseArgs.ticketNumber = body.message.split(\":\")[1];\n                if (body && body.message && body.message.split(':').length > 1) {\n                    app.executeFunction(\"apiResponseDatabase\", apiDatabaseArgs);\n                    return resolve(body.message.split(\":\")[1]);\n                } else {\n                    return resolve(\"\");\n                }\n\n            }\n        })\n    } catch (err) {\n        app.log(err, \"ERROR in generating body crm\");\n        app.log(body)\n        app.sendTextMessage(app.renderMessage(\"claim-error\", {}, 'Sorry there was some error fetching the document'));\n        return resolve();\n    }\n\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-05T05:23:55.277Z",
          "email": "parvez@yellowmessenger.com",
          "name": "crmApi",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7abff",
          "code": "const campaingMapping = {\n    \"health\": \"Chat_Health\",\n    \"car\": \"Chat_FourWheeler\",\n    \"two wheeler\": \"Chat_TwoWheeler\",\n    \"travel\": \"Chat_Travel\",\n    \"accident\": \"Chat_Other\",\n}\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    app.log(app.profile, \"profile\")\n    const name = args.data.username.split(\" \");\n    const date = new Date().toLocaleDateString().split('/');\n    let type = args.data.leadId;\n    if (args.data.leadId === 'car' || args.data.leadId === 'two wheeler') {\n        type = 'motor'\n    }\n    const options = {\n        method: 'POST',\n        url: app.ocrmUrl,\n        headers:\n        {\n            'Postman-Token': '075484f3-a6f2-45bd-bcc4-983c5473bc06',\n            'cache-control': 'no-cache',\n            'Content-Type': 'application/json'\n        },\n        body:\n        {\n            system_name: 'chat',\n            user_name: 'customer_portal_tagic',\n            authkey: 'cust=@2908tagic@2018JXXXguidf@cust_portal23',\n            source: 'Chat Bot',\n            transaction_type: 'motor_nb',\n            set_lob_type: type,\n            product_type: 'null',\n            Req_id: 'REQ_12322',\n            data:\n                [{\n                    leadData:\n                    {\n                        lead_id: '12',\n                        aid: '2856',\n                        gid: '2856',\n                        resultrix_id: '2856',\n                        stage_drop: '2',\n                        first_name: name[0],\n                        last_name: name.length > 1 ? name.slice(1).join(\" \") : \" \",\n                        phone_mobile: args.data.mobileNo,\n                        email_address: args.data.email,\n                        campaign_source: 'Chat Bot',\n                        campaign_medium: 'Chat Bot',\n                        campaign_name: campaingMapping[type],\n                        reason: '',\n                        status_flag: '',\n                        delivery_timestamp: `${date[0]}`,\n                        priority: 'Medium',\n                        keyword_ads_level: 'test',\n                        transaction_type: 'NB',\n                        gcid: '2856',\n                        agency: 'Andro',\n                        adgroup: 'test'\n                    },\n                    LOBData:\n                    {\n                        first_name: name[0],\n                        last_name: name.length > 1 ? name.slice(1).join(\" \") : \" \",\n                        address: app.profile.latitude + ',' + app.profile.longitude,\n                        landmark: '',\n                        pincode: app.profile.value,\n                        city: app.profile.city,\n                        state: app.profile.region,\n                        district: '',\n                        contact_number: args.data.mobileNo,\n                        email_address: args.data.email,\n                        source_of_income: '',\n                        organization_type: '',\n                        organization_name: '',\n                        product: '',\n                        make_payment: '',\n                        net_banking_list: '',\n                        wallet: '',\n                        transaction_id: '',\n                        policy_number: '',\n                        product_plan: '',\n                        total_premium: '',\n                        quotation_no: '',\n                        gender: '',\n                        insured_declared_value: '',\n                        policy_tenure: '',\n                        vehicle_registered_on: '',\n                        occupation: '',\n                        select_vehicle_type: '',\n                        vehicle_status: '',\n                        registration_number: '',\n                        make: '',\n                        model: '',\n                        variant: '',\n                        registration_date: '',\n                        existing_policy_end_date: '',\n                        claim_on_existing_policy: '',\n                        no_of_claims: '',\n                        ncb_in_existing_policy: '',\n                        registration_city: '',\n                        city_used_primarily: '',\n                        non_electrical_acc: '',\n                        liability_to_paid_driver: '',\n                        owner_driver_acc_cover: '',\n                        fuel_type: '',\n                        fuel_kit_sum_insured: '',\n                        unnamed_pass_acc_cover: '',\n                        ncb_protection: '',\n                        rsa: '',\n                        electrical_acc: '',\n                        side_car_option: '',\n                        member_of_auto_asso: '',\n                        member_type: '',\n                        member_number: '',\n                        mem_expiry_date: '',\n                        pan_card_number: '',\n                        vehicle_driven_by: '',\n                        drivers_exp: '',\n                        drivers_dob: '',\n                        engine_number: '',\n                        chasis_number: '',\n                        vehicle_is_financed: '',\n                        agreement_type: '',\n                        financier_name: '',\n                        existing_policy_is: '',\n                        insurance_company_name: '',\n                        old_policy_number: '',\n                        company_branch_code: '',\n                        company_address: '',\n                        company_area_code: '',\n                        total_own_damage_premium: '',\n                        basic_tp_including_tppd: '',\n                        own_damage: '',\n                        workmen_comp: '',\n                        loss_of_personal_belonging: '',\n                        repair_glass_fiber_plastic: '',\n                        total_add_on_premium: '',\n                        basic: '',\n                        total_liability_premium: ''\n                    }\n                }]\n        },\n        json: true\n    };\n    app.log(options, \"OCRM BODy\");\n    app.request.request(options, function (error, response, body) {\n        let apiDatabaseArgs = {\n            tableName: 'ocrm',\n            request: options,\n            response: body,\n            error: error,\n            type: \"Buy online\",\n            elapsedTime: \"\"\n        };\n        if (error) {\n            console.log('error', error);\n            app.executeFunction(\"apiResponseDatabase\", apiDatabaseArgs);\n            return resolve(body.message);\n        } else {\n            app.log('OCRM RESPONSE', body);\n            if (body && body.referenceID) {\n                apiDatabaseArgs.ticketNumber = body.referenceID;\n                app.executeFunction(\"apiResponseDatabase\", apiDatabaseArgs);\n                return resolve(body.referenceID);\n            } else {\n                console.log('error', error);\n                app.executeFunction(\"apiResponseDatabase\", apiDatabaseArgs);\n                return resolve(body.message);\n            }\n\n        }\n    });\n\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-28T06:36:28.995Z",
          "email": "parvez@yellowmessenger.com",
          "name": "ocrmApi",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac00",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.triggerIntent('services',{}).then(()=>{\n        resolve();\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-15T11:09:24.244Z",
          "email": "kishore@yellowmessenger.com",
          "name": "defaultValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac01",
          "code": "return new Promise(function (resolve) {\n    let pdfs;\n    let doc;\n    const steps = app.context.steps;\n    let userData = {\n        username:steps['cust-name'],\n        mobileNo:steps['mobile-number'],\n        email:steps['email-id'],\n        policyNo:'',\n        leadId:'',\n        callerRelation:\"Prospect\",\n        productCategory:\"NP\",\n        product:\"NP\"\n    };\n    if (app.context.steps.type == 'brochure' || app.context.steps.type.indexOf('brochure') > -1) {\n        if (app.context.steps['policy-brochures'] == 'travel' || app.context.steps['policy-brochures'].indexOf('travel')>-1) {\n            pdfs = {\n                \"Travel Guard \": {\n                    \"url\": \"https://www.tataaig.com/content/dam/tagic/PDF/brochures/Travel_Guard.pdf\",\n                    \"title\": \"Travel Guard\",\n                    \"desc\": \"\"\n                },\n                \"Student Guard Plus Policy\": {\n                    \"url\": \"https://www.tataaig.com/content/dam/tagic/PDF/brochures/Student_Guard.pdf\",\n                    \"title\": \"Student Guard Plus Policy\",\n                    \"desc\": \"\"\n                },\n                \"Domestic Travel Guard Policy\": {\n                    \"url\": \"https://www.tataaig.com/content/dam/tagic/PDF/brochures/Domestic_Travel_Guard.PDF\",\n                    \"title\": \"Domestic Travel Guard Policy\",\n                    \"desc\": \"\"\n                },\n                \"Asia Travel Guard Policy\": {\n                    \"url\": \"https://www.tataaig.com/content/dam/tagic/PDF/brochures/Asia_Guard.pdf\",\n                    \"title\": \"Asia Travel Guard Policy\",\n                    \"desc\": \"\"\n                }\n            }\n            doc = app.context.steps['brochure-travel'];\n        }\n        else {\n            pdfs = {\n                \"individual_accident\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/brochures/Individual_accident_and_sickness_hospital_cash_policy_brochurer.pdf\",\n                    title: \"Individual Accident & Sickness Policy\",\n                    desc: \"\"\n                },\n                \"mediprime\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/brochures/MediPrime_Leaflet_New_Sept_Trendz_2016.pdf\",\n                    title: \"MediPrime\",\n                    desc: \"\"\n                },\n                \"mediplus\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/brochures/Mediplus_Brochure-xA-5_Sizex-Trendz.pdf\",\n                    title: \"MediPlus\",\n                    desc: \"\"\n                },\n                \"medisenior\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/brochures/MediSenior_Brochure-xA-5_Sizex-Trendz.pdf\",\n                    title: \"Medisenior\",\n                    desc: \"\"\n                },\n                \"hospital_cash\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/brochures/Individual_accident_and_sickness_hospital_cash_policy_brochurer.pdf\",\n                    title: \"Hospital Cash Policy\",\n                    desc: \"\"\n                },\n                \"wellsurance_family\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/brochures/Artwork_Well_surance_Family_CC_1.pdf\",\n                    title: \"Wellsurance Family Policy\",\n                    desc: \"\"\n                },\n                \"wellsurance_woman\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/brochures/Well_surance_Women_CC_1.pdf\",\n                    title: \"Wellsurance Woman Policy\",\n                    desc: \"\"\n                },\n                \"wellsurance_executive\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/brochures/Artwork_Well_surance_Executive_CC_1.pdf\",\n                    title: \"Wellsurance Executive Policy\",\n                    desc: \"\"\n                },\n                \"mediraksha\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/brochures/MediRaksha_Brochure.pdf\",\n                    title: \"MediRaksha\",\n                    desc: \"\"\n                }\n            }\n            doc = app.context.steps['brochure-health'];\n        }\n    }\n    else {\n        if (app.context.steps['policy-wordings'] == \"motor\") {\n            pdfs = {\n                \"Private Car\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Auto_Secure_Private_Car_Policy_Wordings.pdf\",\n                    title: \"Private Car\",\n                    desc: \"\"\n                },\n                \"Two Wheeler\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Auto_Secure_Two_Wheeler_Package_Policy_With_Addon.pdf\",\n                    title: \"Two Wheeler\",\n                    desc: \"\"\n                },\n                \"Commercial Vehicle\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Auto_Secure_Commercial_Vehicles_Package_Policy.pdf\",\n                    title: \"Commercial Vehicle\",\n                    desc: \"\"\n                }\n            }\n            doc = app.context.steps['wording-motor'];\n        }\n        else if (app.context.steps['policy-wording'] == \"travel\") {\n            pdfs = {\n                \"Travel Guard\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/travel_guard.pdf\",\n                    title: \"Travel Guard\",\n                    desc: \"\"\n                },\n                \"Student Guard Plus Policy \": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/student_guard.pdf\",\n                    title: \"Student Guard Plus Policy\",\n                    desc: \"\"\n                },\n                \"Domestic Travel Guard Policy\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/domestic_travel_guard.pdf\",\n                    title: \"Domestic Travel Guard Policy\",\n                    desc: \"\"\n                },\n                \"Asia Travel Guard Policy\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Asia_Travel_Guard_Policy_Wording.pdf\",\n                    title: \"Asia Travel Guard Policy\",\n                    desc: \"\"\n                }\n            }\n            doc = app.context.steps['wording-travel'];\n        }\n        else if (app.context.steps['policy-wording'] == \"health\") {\n            pdfs = {\n                \"maharaksha\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/maha_Raksha_personal_injury_plan.pdf\",\n                    title: \"Maharaksha - Personal Injury Plan\",\n                    desc: \"\"\n                },\n                \"individual\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/individual_accident_and_sickness_hospital_cash_Policy.pdf\",\n                    title: \"Individual Accident & Sickness Policy\",\n                    desc: \"\"\n                },\n                \"hospital_cash\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/individual_accident_and_sickness_hospital_cash_Policy.pdf\",\n                    title: \"Hospital Cash Policy\",\n                    desc: \"\"\n                },\n                \"hospital_care\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Hospital_Care_Policy.pdf\",\n                    title: \"Hospital Care Policy\",\n                    desc: \"\"\n                },\n                \"complete_care\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Complete_Care_Policy.pdf\",\n                    title: \"Complete Care Policy\",\n                    desc: \"\"\n                },\n                \"accident_guard\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Tata_AIG_Accident_Guard.pdf\",\n                    title: \"Accident Guard Policy\",\n                    desc: \"\"\n                },\n                \"mediprime\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/MediPrime_Policy_Wordings.pdf\",\n                    title: \"MediPrime\",\n                    desc: \"\"\n                },\n                \"mediplus\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/MediPlus_Policy_Wordings.pdf\",\n                    title: \"MediPlus\",\n                    desc: \"\"\n                },\n                \"medisenior\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/MediSenior_Policy_Wordings.pdf\",\n                    title: \"Medisenior\",\n                    desc: \"\"\n                },\n                \"group_mediprime\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Group_Mediprime.pdf\",\n                    title: \"Group Mediprime Policy\",\n                    desc: \"\"\n                },\n                \"wellsurance_family\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Wellsurance_Family_PolicyWordings.pdf\",\n                    title: \"Wellsurance Family Policy\",\n                    desc: \"\"\n                },\n                \"wellsurance_woman\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Wellsurance_Woman_PolicyWordings.pdf\",\n                    title: \"Wellsurance Woman Policy\",\n                    desc: \"\"\n                },\n                \"wellsurance_executive\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Wellsurance_Executive_PolicyWordings.pdf\",\n                    title: \"Wellsurance Executive Policy\",\n                    desc: \"\"\n                },\n                \"income_guard\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/income_guard.pdf\",\n                    title: \"Income Guard Policy\",\n                    desc: \"\"\n                },\n                \"critical_illness\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/criticare.pdf\",\n                    title: \"Critical illnes\",\n                    desc: \"\"\n                },\n                \"accident_shield\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Accident_Shield.pdf\",\n                    title: \"Accident Shield Policy\",\n                    desc: \"\"\n                },\n                \"injury_guard\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Injury_Guard_Policy.pdf\",\n                    title: \"Injury Gaurd Policy\",\n                    desc: \"\"\n                },\n                \"secure_future\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/secured_future_plan.pdf\",\n                    title: \"Secure Future Plan\",\n                    desc: \"\"\n                },\n                \"secure_income_low\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/SecureIncome_Low_PolicyWording.pdf\",\n                    title: \"Secure Income Low Policy\",\n                    desc: \"\"\n                },\n                \"secure_income_high\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/SecureIncomeHigh_PolicyWordings.pdf\",\n                    title: \"Secure Income High Policy\",\n                    desc: \"\"\n                },\n                \"mediraksha\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Mediraksha_Policy_Wordings.pdf\",\n                    title: \"MediRaksha\",\n                    desc: \"\"\n                }\n            }\n            doc = app.context.steps['wording-health'];\n        }\n        else {\n            pdfs = {\n                \"group_credit\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Group_Credit_Secure_Policy_Wordings.pdf\",\n                    title: \"Group Credit secure Policy\",\n                    desc: \"\"\n                },\n                \"home_secure_sfsp\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/SFSP_POLICY_WORDINGS.PDF\",\n                    title: \"Home Secure – SFSP\",\n                    desc: \"\"\n                },\n                \"home_gaurd\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Home_Guard_Plus_Policy_Wording.pdf\",\n                    title: \"Home Gaurd Policy\",\n                    desc: \"\"\n                },\n                \"instachoice\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/Home_Secure_Householder_Instachoice_Policy.pdf\",\n                    title: \"Home Secure (Householders) InstaChoice Policy\",\n                    desc: \"\"\n                },\n                \"home_secure\": {\n                    url: \"https://www.tataaig.com/content/dam/tagic/PDF/policy_wordings/HomeSecure_Policy_wordings.pdf\",\n                    title: \"Home Secure (Householders) Policy\",\n                    desc: \"\"\n                }\n            }\n            doc = app.context.steps['wording-home'];\n        }\n    }\n    app.sendCards([{\n        title: pdfs[doc].title,\n        actions: [{\n            title: \"View Document\",\n            url: pdfs[doc].url\n        }]\n    }]).then(function () {\n        userData.leadId = pdfs[doc].title;\n        app.executeFunction('crmApi', args = { data: userData, status: 'Closed', intentName: steps['type'] });\n        app.pushData({final_response:pdfs[doc].title, transaction:\"Success\"});\n        app.memory.delete('general_query_lead_id');\n        app.triggerIntent('anything-else',{});\n        return;\n    });\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-13T07:25:17.414Z",
          "email": "parvez@yellowmessenger.com",
          "name": "generalEnquiryAction",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac02",
          "code": "return new Promise(function (resolve) {\n    let value = app.data.message.toLowerCase();\n    const steps = app.context.steps;\n    if (value.indexOf('brochure') > -1) {\n        app.setContextParam('policy-wordings', \"\");\n        app.setContextParam('wording-motor', \"\");\n        app.setContextParam('wording-health', \"\");\n        app.setContextParam('wording-travel', \"\");\n        app.setContextParam('wording-home', \"\");\n        app.setContextParam('type', 'policy-brochure');\n        app.pushData({ type: value }, app.context.intent);\n        resolve();\n    }\n    else if (value.indexOf('wording') > -1) {\n        app.setContextParam('policy-brochures', \"\");\n        app.setContextParam('brochure-travel', \"\");\n        app.setContextParam('brochure-health', \"\");\n        app.setContextParam('type', \"policy-wordings\");\n        app.pushData({ type: value }, app.context.intent);\n        resolve();\n    } else if (value.indexOf('locators') > -1) {\n        app.pushData({ transaction: \"Moved to Locators\" }, app.context.intent);\n        app.pushData({ 'username': steps['cust-name'], 'email': steps['email-id'], 'mobile': steps['mobile-number'], 'transaction': 'Abondened' }, 'tie-up-locations');\n        app.triggerIntent('tie-up-locations', {}, { 'cust-name': steps['cust-name'], 'email-id': steps['email-id'], 'mobile-number': steps['mobile-number'] }).then(() => {\n            app.memory.delete('general_query_lead_id');\n            return;\n        })\n    }\n    else {\n        app.sendQuickReplies({\n            title: app.renderMessage('choose-below-options', {}, \"Please choose the type to proceed.\"),\n            options: [\n                {\n                    title: \"Policy Brochures\",\n                    text: \"brochures\"\n                },\n                {\n                    title: \"Policy Wordings \",\n                    text: \"wordings\"\n                },\n                {\n                    title: \"Tie-ups & Locators\",\n                    text: \"locators\"\n                }\n            ]\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-05T20:04:53.028Z",
          "email": "parvez@yellowmessenger.com",
          "name": "gqTypeValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac03",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    let policyNumber = app.data.message.split('-')[1];\n    app.validate(policyNumber).then(policy => {\n        app.sendTextMessage(policy)\n        if (/^\\d{10}$/g.test(policy)) {\n            app.sendTextMessage('inside if')\n            let args = {\n                es_query: {\n                    query: {\n                        match: {\n                            policy_number: policy\n                        }\n                    }\n                },\n                table: \"claim_intimation_lead\"\n            }\n            app.executeFunction('searchQuery', args = args).then((result) => {\n                app.sendTextMessage(JSON.stringify(result))\n                let condition = new Date(new Date(result.updatedDate).getTime() + 60 * 60 * 24 * 1000) > new Date();\n                app.sendTextMessage(condition.toString());\n                if (result && result.policy_number === policy && result.transaction != 'Abondened' && !condition && !app.UAT_ENV) {\n                    app.sendTextMessage(app.renderMessage('claim-already-registered', { policyNo: result.policy_number }, '')).then(() => {\n                        app.triggerIntent('anything-else', {});\n                        return resolve;\n                    })\n                } else {\n                    app.sendTextMessage('in else')\n                    app.pushData({ policy_number: policy, transaction: 'Abondened', claim_category: app.context.steps['claim-category'], motor_type: app.context.steps['motor-type'] }, app.context.intent)\n                    return resolve();\n                }\n            })\n\n        } else {\n            app.sendTextMessage('in else')\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"incorrect_policy_number\", {}, \"Please enter a valid 10 digit policy number. \\n(for eg: 0155009013)\")\n            })\n        }\n    });\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-12T07:48:29.074Z",
          "email": "parvez@yellowmessenger.com",
          "name": "crmTest",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac04",
          "code": "return new Promise(function (resolve) {\n    let value = app.data.message.toLowerCase();\n    if (value.indexOf('travel') > -1) {\n        app.pushData({ policy_brochure: value }, app.context.intent);\n        app.setContextParam('brochure-health', \"\");\n        app.setContextParam('policy-brouchure', \"travel\")\n        resolve();\n    }\n    else if (value.indexOf('health') > -1) {\n        app.pushData({ policy_brochure: value }, app.context.intent);\n        app.setContextParam('brochure-travel', \"\");\n        app.setContextParam('policy-brouchure', \"health\")\n        resolve();\n    }\n    else {\n        app.sendQuickReplies({\n            title: app.renderMessage('choose-below-options',{},\"Please choose the type to proceed.\"),\n            options: [\n                {\n                    title: \"Travel Products\",\n                    text: \"travel\"\n                },\n                {\n                    title: \"Accident and Health Products \",\n                    text: \"health\"\n                }\n            ]\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-03T10:48:53.708Z",
          "email": "parvez@yellowmessenger.com",
          "name": "policyBrouchureValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac05",
          "code": "return new Promise(function (resolve) {\n    let value = app.data.message.toLowerCase();\n    if (value.indexOf('travel') > -1) {\n        app.pushData({ policy_wordings: value }, app.context.intent);\n        app.setContextParam('policy-wording', 'travel');\n        app.setContextParam('wording-motor', \"\");\n        app.setContextParam('wording-health', \"\");\n        app.setContextParam('wording-home', \"\");\n        resolve();\n    }\n    else if (value.indexOf('motor') > -1) {\n        app.pushData({ policy_wordings: value }, app.context.intent);\n        app.setContextParam('policy-wording', 'motor');\n        app.setContextParam('wording-travel', \"\");\n        app.setContextParam('wording-health', \"\");\n        app.setContextParam('wording-home', \"\");\n        resolve();\n    }\n    else if (value.indexOf('health') > -1) {\n        app.pushData({ policy_wordings: value }, app.context.intent);\n        app.setContextParam('policy-wording', 'health');\n        app.setContextParam('wording-travel', \"\");\n        app.setContextParam('wording-motor', \"\");\n        app.setContextParam('wording-home', \"\");\n        resolve();\n    }\n    else if (value.indexOf('home') > -1) {\n        app.pushData({ policy_wordings: value }, app.context.intent);\n        app.setContextParam('policy-wording', 'home');\n        app.setContextParam('wording-travel', \"\");\n        app.setContextParam('wording-motor', \"\");\n        app.setContextParam('wording-health', \"\");\n        resolve();\n    }\n    else {\n        app.sendQuickReplies({\n            title: app.renderMessage('choose-below-options',{},\"Please choose the type to proceed.\"),\n            options: [\n                {\n                    title: \"Motor Products\",\n                    text: \"motor\"\n                },\n                {\n                    title: \"Travel Products \",\n                    text: \"travel\"\n                },\n                {\n                    title: \"Accident and Health Products \",\n                    text: \"health\"\n                },\n                {\n                    title: \"Home Insurance Products\",\n                    text: \"home\"\n                }\n            ]\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-03T18:09:04.601Z",
          "email": "parvez@yellowmessenger.com",
          "name": "policyWordingValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac06",
          "code": "\nreturn new Promise(function (resolve) {\n    let value = app.data.message.toLowerCase();\n    let a = ['travel guard', 'student guard plus policy', 'domestic travel guard policy', 'asia travel guard policy'];\n    app.log(value, \"value\");\n    if (a.indexOf(value.toLowerCase().trim()) > -1) {\n        app.pushData({ brochure_travel: value }, app.context.intent);\n        return resolve();\n    }\n    else {\n        app.sendQuickReplies({\n            title: app.renderMessage('choose-below-options',{},\"Please choose the type to proceed.\"),\n            options: [\n                {\n                    title: \"Travel Guard \",\n                    text: \"Travel Guard\"\n                },\n                {\n                    title: \"Student Guard Plus Policy \",\n                    text: \"Student Guard Plus Policy\"\n                },\n                {\n                    title: \"Domestic Travel Guard Policy \",\n                    text: \"Domestic Travel Guard Policy\"\n                },\n                {\n                    title: \"Asia Travel Guard Policy\",\n                    text: \"Asia Travel Guard Policy\"\n                }\n            ]\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-13T07:01:07.979Z",
          "email": "parvez@yellowmessenger.com",
          "name": "brochureTravelValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac07",
          "code": "return new Promise(function (resolve) {\n    let value = app.data.message.toLowerCase().trim();\n    let a = ['individual_accident', 'mediprime', 'mediplus', 'medisenior', 'hospital_cash', 'wellsurance_family', 'wellsurance_woman', 'wellsurance_executive', 'mediraksha'];\n    if (a.includes(value) > -1) {\n        app.pushData({ brochure_health: value }, app.context.intent);\n        app.setContextParam('brochure-health', value)\n        resolve();\n    }\n    else {\n        app.sendQuickReplies({\n            title: app.renderMessage('choose-below-options',{},\"Please choose the type to proceed.\"),\n            options: [\n                {\n                    title: \"Individual Accident & Sickness Policy\",\n                    text: \"individual_accident \"\n                },\n                {\n                    title: \"MediPrime\",\n                    text: \"MediPrime\"\n                },\n                {\n                    title: \"MediPlus\",\n                    text: \"MediPlus\"\n                },\n                {\n                    title: \"Medisenior\",\n                    text: \"Medisenior\"\n                },\n                {\n                    title: \"Hospital Cash Policy \",\n                    text: \"hospital_cash\"\n                },\n                {\n                    title: \"Wellsurance Family Policy\",\n                    text: \"wellsurance_family\"\n                },\n                {\n                    title: \"Wellsurance Woman Policy\",\n                    text: \"wellsurance_woman\"\n                },\n                {\n                    title: \"Wellsurance Executive Policy\",\n                    text: \"wellsurance_executive\"\n                },\n                {\n                    title: \"MediRaksha\",\n                    text: \"MediRaksha\"\n                },\n            ]\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-04T05:46:03.256Z",
          "email": "parvez@yellowmessenger.com",
          "name": "brochureHealthValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac08",
          "code": "return new Promise(function (resolve) {\n    let value = app.data.message.toLowerCase().trim();\n    let a = ['maharaksha', 'individual', 'hospital_cash', 'hospital_care', 'complete_care', 'accident_guard',\n        'mediprime', 'mediplus', 'medisenior', 'group_mediprime', 'wellsurance_family', 'wellsurance_woman', 'wellsurance_executive',\n        'income_guard', 'critical_illness', 'accident_shield', 'injury_guard', 'secure_future', 'secure_income_low', 'secure_income_high', 'mediraksha'];\n    if (a.indexOf(value) > -1) {\n        app.memory.delete(\"more\");\n        app.pushData({ wording_health: value }, app.context.intent);\n        resolve();\n    }\n    else if (value == \"more\") {\n        /*\n        Maharaksha - Personal Injury Plan : maharaksha,Individual Accident & Sickness Policy : individual,Hospital Cash Policy : hospital_cash,Hospital Care Policy : hospital_care,Complete Care Policy : complete_care,Accident Guard Policy : accident_guard,MediPrime : mediprime,MediPlus : mediplus,Medisenior : medisenior,Group Mediprime Policy : group_mediprime,Wellsurance Family Policy : wellsurance_family,Wellsurance Woman Policy : wellsurance_woman,Wellsurance Executive Policy : wellsurance_executive,Income Guard Policy : income_guard,Critical illness : critical_illness,Accident Shield Policy : accident_shield,Injury Guard Policy : injury_guard,Secure Future Plan : secure_future,Secure Income Low Policy : secure_income_low,Secure Income High Policy : secure_income_high,MediRaksha : mediraksha\n        */\n        let health = [{ title: \"Maharaksha - Personal Injury Plan\", text: \"maharaksha\" }, { title: \"Individual Accident & Sickness Policy\", text: \"individual\" }, { title: \"Hospital Cash Policy\", text: \"hospital_cash\" }, { title: \"Hospital Care Policy\", text: \"hospital_care\" }, { title: \"Complete Care Policy\", text: \"complete_care\" },\n        { title: \"Accident Guard Policy\", text: \"accident_guard\" }, { title: \"MediPrime\", text: \"mediprime\" }, { title: \"MediPlus\", text: \"mediplus\" }, { title: \"Medisenior\", text: \"medisenior\" }, { title: \"Group Mediprime Policy\", text: \"group_mediprime\" },\n        { title: \"Wellsurance Family Policy\", text: \"wellsurance_family\" }, { title: \"Wellsurance Woman Policy\", text: \"wellsurance_woman\" }, { title: \"Wellsurance Executive Policy\", text: \"wellsurance_executive\" }, { title: \"Income Guard Policy\", text: \"income_guard\" }, { title: \"Critical illness\", text: \"critical_illness\" },\n        { title: \"Accident Shield Policy\", text: \"accident_shield\" }, { title: \"Injury Guard Policy\", text: \"injury_guard\" }, { title: \"Secure Future Plan\", text: \"secure_future\" }, { title: \"Secure Income Low Policy\", text: \"secure_income_low\" }, { title: \"Secure Income High Policy\", text: \"secure_income_high\" }, { title: \"MediRaksha\", text: \"mediraksha\" }];\n        app.memory.get(\"more\").then(function (more) {\n            more = parseInt(more);\n            let start = more * 5;\n            let end = start + 5 + ((more == 3) ? 1 : 0);\n            let options = health.slice(start, end);\n            options.push({\n                title: \"More\",\n                text: \"more\"\n            });\n            app.log(start, \"start\");\n            app.log(end, \"end\");\n            more = (more + 1) % 4;\n            app.memory.set(\"more\", more.toString());\n            app.sendQuickReplies({\n                title: \"\",\n                options: options\n            });\n        }).catch(function (err) {\n            //firt time more is pressed\n            let more = 1;\n            let start = more * 5;\n            let end = start + 5;\n            let options = health.slice(start, end);\n            options.push({\n                title: \"More\",\n                text: \"more\"\n            });\n            more = (more + 1) % 4;\n            app.memory.set(\"more\", more.toString());\n            app.sendQuickReplies({\n                title: \"\",\n                options: options\n            });\n        });\n    }\n    else {\n        app.memory.delete(\"more\");\n        let health = [{ title: \"Maharaksha - Personal Injury Plan\", text: \"maharaksha\" }, { title: \"Individual Accident & Sickness Policy\", text: \"individual\" }, { title: \"Hospital Cash Policy\", text: \"hospital_cash\" }, { title: \"Hospital Care Policy\", text: \"hospital_care\" }, { title: \"Complete Care Policy\", text: \"complete_care\" },\n        { title: \"Accident Guard Policy\", text: \"accident_guard\" }, { title: \"MediPrime\", text: \"mediprime\" }, { title: \"More\", text: \"more\" }];\n        app.sendQuickReplies({\n            title:app.renderMessage(\"choose-below-options\",{}, \"\"),\n            options:health\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-03T12:28:51.325Z",
          "email": "parvez@yellowmessenger.com",
          "name": "wordingHealthValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac09",
          "code": "return new Promise(function (resolve) {\n    let value = app.data.message;\n    let a = ['Private Car', 'Two Wheeler', 'Commercial Vehicle'];\n    if (a.includes(value)) {\n        app.pushData({wording_motor:value}, app.context.intent);\n        resolve();\n    }\n    else {\n        app.sendQuickReplies({\n            title: app.renderMessage('choose-below-options',{},\"Please choose the type to proceed.\"),\n            options: [\n                {\n                    title: \"Private Car\",\n                    text: \"Private Car\"\n                },\n                {\n                    title: \"Two Wheeler \",\n                    text: \"Two Wheeler\"\n                },\n                {\n                    title: \"Commercial Vehicle\",\n                    text: \"Commercial Vehicle\"\n                },\n            ]\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-03T10:48:28.123Z",
          "email": "parvez@yellowmessenger.com",
          "name": "wordingMotorValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac0a",
          "code": "return new Promise(function (resolve) {\n    let value = app.data.message;\n    let a = ['Travel Guard', 'Student Guard Plus Policy ', 'Domestic Travel Guard Policy', 'Asia Travel Guard Policy'];\n    if (a.includes(value)) {\n        app.pushData({wording_travel:value}, app.context.intent);\n        resolve();\n    }\n    else {\n        app.sendQuickReplies({\n            title: app.renderMessage('choose-below-options',{},\"Please choose the type to proceed.\"),\n            options: [\n                {\n                    title: \"Travel Guard\",\n                    text: \"Travel Guard\"\n                },\n                {\n                    title: \"Student Guard Plus Policy  \",\n                    text: \"Student Guard Plus Policy \"\n                },\n                {\n                    title: \"Domestic Travel Guard Policy\",\n                    text: \"Domestic Travel Guard Policy\"\n                },\n                {\n                    title:\"Asia Travel Guard Policy\",\n                    text:\"Asia Travel Guard Policy\"\n                }\n            ]\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-03T10:48:32.794Z",
          "email": "parvez@yellowmessenger.com",
          "name": "wordingTravelValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac0b",
          "code": "return new Promise(function (resolve) {\n    let value = app.data.message.toLowerCase().trim();\n    let a = ['group_credit', 'home_secure_sfsp', 'home_gaurd', 'instachoice', 'home_secure'];\n    if (a.indexOf(value) > -1) {\n        app.pushData({wording_home:value}, app.context.intent);\n        resolve();\n    }\n    else {\n        app.sendQuickReplies({\n            title: app.renderMessage('choose-below-options',{},\"Please choose the type to proceed.\"),\n            options: [\n                {\n                    title: \"Group Credit secure Policy \",\n                    text: \"group_credit\"\n                },\n                {\n                    title: \"Home Secure – SFSP\",\n                    text: \"home_secure_sfsp\"\n                },\n                {\n                    title: \"Home Gaurd Policy\",\n                    text: \"home_gaurd\"\n                },\n                {\n                    title:\"Home Secure (Householders) InstaChoice Policy \",\n                    text:\"instachoice\"\n                },\n                {\n                    title:\"Home Secure (Householders) Policy\",\n                    text:\"home_secure\"\n                }\n            ]\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-03T18:07:15.750Z",
          "email": "parvez@yellowmessenger.com",
          "name": "wordingHomeValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac0c",
          "code": "const successMessage = (cards, userData, intentName) => {\n    return new Promise(resolve => {\n        app.sendCards(cards).then(() => {\n            app.executeFunction('crmApi', { data: userData, status: 'Closed', intentName: intentName }).then((ticketNumber) => {\n                app.pushData({ transaction: 'success', ticket_number: ticketNumber }, app.context.intent).then(() => {\n                    app.memory.delete('tieuplocations_leads_id');\n                    if (app.source === 'facebook') {\n                        app.clearContext();\n                        app.data.message = 'anything else';\n                        return app.start();\n                    } else {\n                        app.triggerIntent('anything-else', {});\n                        return resolve();\n                    }\n                })\n            })\n        })\n    })\n}\nconst failureMessage = (userData, intentName, location) => {\n    return new Promise(resolve => {\n        app.executeFunction('crmApi', { data: userData, status: 'Open', intentName: intentName }).then((ticketNumber) => {\n            app.pushData({ transaction: intentName + ' Not Found', ticket_number: ticketNumber }, app.context.intent).then(() => {\n                app.memory.delete('tieuplocations_leads_id');\n                app.triggerIntent('anything-else', {});\n                return resolve();\n            })\n        })\n    })\n}\nconst findNearest = (tableName, location, userData, locationName) => {\n    return new Promise((resolve, reject) => {\n        // Your logic goes here\n        app.sendTextMessage(app.renderMessage('fetch-garages', { type: tableName }, \"\")).then(() => {\n            let es_query = {\n                \"from\": 0,\n                \"size\": 10,\n                \"query\": {\n                    \"bool\": {\n                        \"must\": {\n                            \"match_all\": {}\n                        },\n                        \"filter\": {\n                            \"geo_distance\": {\n                                \"latlon\": {\n                                    \"lat\": location.lat,\n                                    \"lon\": location.lon\n                                },\n                                \"distance\": \"50km\"\n                            }\n                        },\n                    }\n                },\n                \"sort\": [\n                    {\n                        \"_geo_distance\": {\n                            \"latlon\": {\n                                \"lat\": location.lat,\n                                \"lon\": location.lon\n                            },\n                            \"order\": \"asc\",\n                            \"unit\": \"km\",\n                            \"distance_type\": \"plane\"\n                        }\n                    }\n                ]\n            };\n            app.executeFunction('searchTable', { table: tableName, es_query: es_query }).then((result) => {\n                if (!result) {\n                    es_query = {\n                        \"query\": {\n                            \"multi_match\": {\n                                \"query\": locationName,\n                                \"fields\": [\"line_1_address\", \"line_2_address\", \"line_3_address\", \"line_4_address\", \"line_5_address\", \"city_town_name\", \"alt_name\", \"branch_name\", \"address\"]\n                            }\n                        }\n                    }\n                    app.executeFunction('searchTable', { table: tableName, es_query: es_query }).then((result) => {\n                        if (!result) {\n                            app.sendTextMessage(app.renderMessage('no-service-centers', { type: tableName }, '')).then(() => {\n                                failureMessage(userData, 'garage-location', app.context.steps.location);\n                                return;\n                            })\n                        } else if (tableName === 'hospitals') {\n                            let cards = app._.map(result, function (hit) {\n                                let card = {\n                                    title: hit._source.hospital_name,\n                                    text: `Address : ${hit._source.hospital_address}\\n\\nContact person : ${hit._source.contact_person}\\n Contact number : ${hit._source.contact_number}`,\n                                }\n                                return card;\n                            })\n                            console.log(cards);\n                            return resolve(cards);\n                        } else {\n                            let cards = app._.map(result, function (hit) {\n                                let card = {\n                                    title: hit._source.branchName,\n                                    text: `Address : ${hit._source.address}\\n Contact number : ${hit._source.contactno}`,\n                                }\n                                return card;\n                            });\n                            return resolve(cards);\n                        }\n                    })\n                } else if (tableName === 'hospitals') {\n                    let cards = app._.map(result, function (hit) {\n                        let card = {\n                            title: hit._source.hospital_name,\n                            text: `Address : ${hit._source.hospital_address}\\n\\nContact person : ${hit._source.contact_person}\\n Contact number : ${hit._source.contact_number}`,\n                        }\n                        return card;\n                    })\n                    console.log(cards);\n                    return resolve(cards);\n                } else {\n                    let cards = app._.map(result, function (hit) {\n                        let card = {\n                            title: hit._source.branchName,\n                            text: `Address : ${hit._source.address}\\n Contact number : ${hit._source.contactno}`,\n                        }\n                        return card;\n                    });\n                    return resolve(cards);\n                }\n            })\n        });\n    })\n};\nreturn new Promise(resolve => {\n    // Your logic goes here\n    const steps = app.context.steps;\n    app.log(steps, \"steps\");\n    let userDate = {\n        username: steps['cust-name'],\n        mobileNo: steps['mobile-number'],\n        email: steps['email'],\n        policyNo: '',\n        leadId: steps['location'],\n        callerRelation: \"Others\"\n    };\n    let es_query = {};\n    switch (steps.type) {\n        case 'garages':\n            es_query = {\n                \"query\": {\n                    \"multi_match\": {\n                        \"query\": steps.location,\n                        \"fields\": [\"line_1_address\", \"line_2_address\", \"line_3_address\", \"line_4_address\", \"line_5_address\", \"city_town_name\", \"alt_name\"]\n                    }\n                }\n            }\n            app.sendTextMessage(app.renderMessage('fetch-garages', { type: steps.type }, \"\")).then(() => {\n                app.executeFunction('searchTable', { table: 'garages', es_query: es_query }).then((result) => {\n                    if (!result) {\n                        app.sendTextMessage(app.renderMessage('no-service-centers', { type: 'garages' }, '')).then(() => {\n                            failureMessage(userData, 'garage-location', steps.location);\n                            return resolve();\n                        })\n                    } else {\n                        let card;\n                        let cards = app._.map(result, function (hit) {\n                            card = {\n                                title: hit._source.arg_name,\n                                text: `Address : ${hit._source.line_1_address}\\n${hit._source.line_1_address}\\n${hit._source.line_1_address}\\n${hit._source.post_cd}\\n \\nContact person : ${hit._source.contact_person}\\n Contact number : ${hit._source.mobile_no_garage}`,\n                            }\n                            return card;\n                        })\n                        console.log(cards);\n                        successMessage(cards, userDate, 'garage-location').then(() => {\n                            return resolve();\n                        });\n                    }\n                });\n            });\n            break;\n        case 'hospitals':\n            findNearest('hospitals', steps.latlong, userDate, steps.location).then(cards => {\n                successMessage(cards, userDate, 'hospital-location').then(() => {\n                    return resolve();\n                })\n            })\n            break;\n        case 'branches':\n            findNearest('branches', steps.latlong, userDate, steps.location).then(cards => {\n                successMessage(cards, userDate, 'branch-location').then(() => {\n                    return resolve();\n                })\n            })\n            break;\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-02T11:29:10.607Z",
          "email": "parvez@yellowmessenger.com",
          "name": "tieUpAction",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac0d",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    let value = app.data.message;\n    if (/^.*(garages).*$/ig.test(value)) {\n        app.setContextParam('type', 'garages');\n        app.pushData({type:'garages'}, app.context.intent);\n        return resolve();\n    } else if (/^.*(hospitals).*$/ig.test(value)) {\n        app.setContextParam('type', 'hospitals');\n        app.pushData({type:'hospitals'}, app.context.intent);\n        return resolve();\n    } else if (/^.*(branches).*$/ig.test(value)) {\n        app.setContextParam('type', 'branches');\n        app.pushData({type:'branches'}, app.context.intent);\n        return resolve();\n    } else {\n        app.sendQuickReplies({\n            title: app.renderMessage('choose-below-options', {}, ''),\n            options: [\n                {\n                    title: \"Tie-up Garages\",\n                    text: \"garages\"\n                },\n                {\n                    title: \"Tie-up Hospitals\",\n                    text: \"hospitals\"\n                },\n                {\n                    title: \"Branches\",\n                    text: \"branches\"\n                },\n            ]\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-24T08:44:53.669Z",
          "email": "parvez@yellowmessenger.com",
          "name": "tieUpTypeValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac0e",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    if (app.data && app.data.location && app.data.location.lat && app.data.location.lon) {\n        let opt = {\n            \"method\": \"GET\",\n            \"url\": `https://maps.googleapis.com/maps/api/geocode/json?latlng=${app.data.location.lat},${app.data.location.lon}&key=AIzaSyBrojomjYgAZN_AdBq-Bk7xZTnZQ1eA7KU`\n        }\n        app.request.request(opt, function (err, res, body) {\n            let data = JSON.parse(res.body).results[0].address_components;\n            if (err) {\n                app.log(err, \"Error from GEOLOCATION\");\n                return resolve({\n                    success: false,\n                    question: app.renderMessage('some-problem', {}, \"There was some problem getting your location please try again.\")\n                })\n            } else {\n                data.forEach(component => {\n                    if (component.types.includes('locality')) {\n                        app.setContextParam('latlong', app.data.location);\n                        app.setContextParam('location', component.long_name);\n                        app.pushData({ location: component.long_name }, app.context.intent);\n                        return resolve();\n                    }\n                })\n            }\n        });\n    } else if (app.data.message) {\n        const options = {\n            method: 'GET',\n            url: 'https://maps.googleapis.com/maps/api/geocode/json',\n            qs:\n            {\n                address: app.data.message,\n                key: 'AIzaSyBrojomjYgAZN_AdBq-Bk7xZTnZQ1eA7KU'\n            },\n            headers:\n            {\n                'Postman-Token': '2a9c0c07-4eaa-4b45-8f47-383c3dfd6b90',\n                'cache-control': 'no-cache'\n            }\n        };\n\n        app.request.request(options, function (error, response, body) {\n            if (error) {\n                app.log(error, \"ERror in geoCOrdinates\");\n                app.sendTextMessage(app.renderMessage('claim-error', {}, '')).then(() => {\n                    app.sendQuickReplies({\n                        title: app.renderMessage('share-location', { type: app.context.steps.type }, ''),\n                        options: [\n                            {\n                                title: \"Share Location\",\n                                location: true\n                            }\n                        ]\n                    });\n                })\n            } else {\n                if(typeof body === 'string'){\n                    body = JSON.parse(body);\n                }\n                if (body && body.results && body.results[0].geometry && body.results[0].geometry.location) {\n                    body = body.results[0].geometry.location;\n                    app.setContextParam('latlong', {lat:body.lat, lon:body.lng})\n                    app.setContextParam('location', app.data.message);\n                    app.pushData({ location: app.data.message }, app.context.intent);\n                    return resolve();\n                } else {\n                    app.sendQuickReplies({\n                        title: app.renderMessage('share-location', { type: app.context.steps.type }, ''),\n                        options: [\n                            {\n                                title: \"Share Location\",\n                                location: true\n                            }\n                        ]\n                    });\n                }\n            }\n        });\n    } else {\n        app.sendQuickReplies({\n            title: app.renderMessage('share-location', { type: app.context.steps.type }, ''),\n            options: [\n                {\n                    title: \"Share Location\",\n                    location: true\n                }\n            ]\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-24T08:44:45.212Z",
          "email": "parvez@yellowmessenger.com",
          "name": "tieUplocationValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac0f",
          "code": "return new Promise(function(resolve){\n  if(app.term){\n    app.memory.get(\"state_id\").then(state_id => {\n      app.log(state_id, \"STATE ID\");\n      app.dataStore.search({\n        table: \"districts\",\n        body: {\n          \"query\": {\n            \"bool\": {\n              \"must\":\n                {\"regexp\": { \"District_Name\": app.term.toLowerCase() + \".*\" }}\n              ,\n              \"filter\":\n                {\n                  \"match\": {\"District_State_FK\": state_id},\n                }\n            }\n          }\n        }\n      }).then((result) => {\n        return resolve(app._.map(result.hits.hits, function (hit) {\n          return [hit._source.District_Name, hit._source.District_Name + \"$\" + hit._source.District_ID_PK];\n        }))\n\n      },(e)=>{\n        app.log(e,\"error\");\n      })\n\n    })\n\n  }else{  resolve([]) }\n})",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-04T07:47:21.938Z",
          "email": "parvez@yellowmessenger.com",
          "name": "tieUpLocationAutoComplete",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac10",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.dataStore.search({\n        table: args.table,\n        body: args.es_query\n    }).then((result) => {\n        if (result && result.hits.hits && result.hits.hits.length > 0) {\n            return resolve(result.hits.hits);\n        } else {\n            return resolve(false);\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-05T20:00:33.973Z",
          "email": "parvez@yellowmessenger.com",
          "name": "searchTable",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac11",
          "code": "const askName = () => {\n    return app.sendQuickReplies({\n        title: app.renderMessage('email', {}, \"Please enter your registered email id\"),\n        options: [{\n            title: \"I don't have email Id\",\n            text: \"noemailid\"\n        }]\n    });\n}\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    app.memory.get('userDetails').then(user => {\n        user = JSON.parse(user);\n        if (user.email) {\n            app.sendQuickReplies({\n                title: app.renderMessage('email', {}, \"Please enter your registered email id\"),\n                options: [\n                    {\n                        title: \"I don't have email Id\",\n                        text: \"noemailid\"\n                    },\n                    {\n                        title: user.email,\n                        text: user.email\n                    }]\n            });\n            return resolve();\n        } else {\n            askName()\n            return resolve();\n        }\n    }).catch(err => {\n        askName()\n        return resolve();\n    })\n\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-11T04:56:30.769Z",
          "email": "parvez@yellowmessenger.com",
          "name": "claimEmailQF",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac12",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    if (app.prediction.global_model.intent === 'yes' && app.prediction.global_model.confidence > 0.85) {\n        app.pushData({ insured_person: \"Insured\" }, app.context.intent);\n        app.setContextParam('insured', 'Insured');\n        return resolve();\n    } else {\n        app.pushData({ insured_person: \"Garage\" }, app.context.intent);\n         app.setContextParam('insured', 'Garage');\n        return resolve();\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-15T07:47:40.676Z",
          "email": "parvez@yellowmessenger.com",
          "name": "claimInsuredValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac13",
          "code": "const setMemory = () => {\n    return new Promise(resolve => {\n        app.memory.get('userDetails').then((result) => {\n            if (typeof result === 'string') {\n                result = JSON.parse(result);\n            }\n            app.setContextParam('cust-name', result.name).then(() => {\n                app.setContextParam('mobile-number', result.agentMobile).then(() => {\n                    app.setContextParam('email-id', result.email).then(() => {\n                        app.pushData({ 'username': result.name, 'email': result.email, 'mobile': result.agentMobile, 'transaction': 'Abondened' }, 'tie-up-locations').then(() => {\n                            return resolve();\n                        })\n                    })\n                })\n            })\n        }).catch(err => {\n            return resolve();\n        })\n    })\n}\n\nconst setCity = (prediction) => {\n    return new Promise(resolve => {\n        if (prediction && prediction.global_entities && prediction.global_entities.length > 1) {\n            app._.forEach(prediction.global_entities, (element) => {\n                if (element.label === 'city') {\n                    app.executeFunction('googleNameToLatLon', { city: element.text }).then(latLong => {\n                        app.setContextParam('latlong', latLong).then(() => {\n                            app.setStep('location', element.text).then(() => {\n                                app.pushData({ location: element.text }, app.context.intent).then(() => {\n                                    return resolve();\n                                })\n                            })\n                        })\n                    });\n                }\n            });\n        } else if (prediction && prediction.entities && prediction.entities.location && prediction.entities.location.length > 0 && prediction.entities.location.confidence > 0.8) {\n            app.executeFunction('googleNameToLatLon', { city: prediction.entities.location[0].text }).then(latLong => {\n                app.setStep('latlong', latLong)\n                app.pushData({ location: prediction.entities.location[0].text }, app.context.intent).then(() => {\n                    app.setContextParam('location', prediction.entities.location[0].text).then(() => {\n                        return resolve();\n                    })\n                })\n            });\n        }else{\n            return resolve()\n        }\n    })\n}\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    app.memory.delete('othersLanguage');\n    app.options.targetLanguage = 'en';\n    const value = app.data.message;\n    // Your logic goes here\n    const prediction = app.prediction;\n    app.log(prediction, \"prediction\")\n    setCity(prediction).then(() => {\n        if (/^.*(garage|garages).*$/ig.test(value)) {\n            app.pushData({ type: 'Garages' }, app.context.intent);\n            app.setContextParam('type', 'garages');\n            setMemory().then(() => {\n                return resolve();\n            });\n        } else if (/^.*(hospitals|hospital).*$/ig.test(value)) {\n            app.pushData({ type: 'Hospitals' }, app.context.intent);\n            app.setContextParam('type', 'hospitals');\n            setMemory().then(() => {\n                return resolve();\n            });\n        } else if (/^.*(branches|branch).*$/ig.test(value)) {\n            app.pushData({ type: 'Branches' }, app.context.intent);\n            app.setContextParam('type', 'branches');\n            setMemory().then(() => {\n                return resolve();\n            });\n        } else {\n            setMemory().then(() => {\n                return resolve();\n            });\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-24T09:39:52.904Z",
          "email": "parvez@yellowmessenger.com",
          "name": "tieupInit",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac14",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.sendQuickReplies({\n        title:\"Please tell us where do you want to locate the \"+app.context.steps['type'],\n        options:[\n            {\n                title:\"Share Location\",\n                location:true\n            }\n        ]\n    }).then(()=>{\n        return resolve();\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-12T10:18:20.153Z",
          "email": "parvez@yellowmessenger.com",
          "name": "takeLocation",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac15",
          "code": "return new Promise(resolve => {\n    try {\n        if (app.source === 'facebook') {\n            app.clearContext();\n            app.sendTextMessage('Sorry, This facility is not available on facebook yet, but you can access it from the web.').then(() => {\n                app.sendTextMessage('Please follow the below link or you can access our other services.').then(() => {\n                    app.sendCards([\n                        {\n                            title: 'Tara',\n                            text: '',\n                            actions: [\n                                {\n                                    title: 'Navigate',\n                                    url: 'https://yellow.chat/tata_aig/'\n                                }\n                            ]\n                        },\n                        {\n                            title: 'Services',\n                            text: '',\n                            actions: [\n                                {\n                                    title: 'Show options',\n                                    url: 'services'\n                                }\n                            ]\n                        },\n                    ]).then(() => {\n                        return resolve();\n                    })\n                });\n            });\n        } else {\n            app.memory.delete('othersLanguage');\n            app.options.targetLanguage = 'en';\n            if (new Date(app.holiday).toDateString() === new Date().toDateString()) {\n                app.sendTextMessage('Thank you for contacting us.').then(() => {\n                    app.sendTextMessage(app.holidayMessage).then(() => {\n                        app.triggerIntent('anything-else', {});\n                        return;\n                    })\n                })\n            } else {\n                let date = new Date().toLocaleString(\"en-US\", { hour12: false, timeZone: \"Asia/Calcutta\" });\n                let time = date.split(',')[1].trim();\n                let hour = time.split(':')[0];\n                app.log(hour, \"HOURS\");\n                let day = new Date(date).getDay();\n                if ((day == 0 || hour > 17 || hour < 9) && !app.UAT_ENV) {\n                    app.sendTextMessage(app.renderMessage('preinspection-off', {}, \"Sorry, we won’t be able to process your request at the moment. Please try again on Mon – Sat (9 AM to 6 PM) for this query. Thank you for your patience.\"));\n                    app.clearContext();\n                    app.triggerIntent(\"anything-else\", {});\n                    return;\n                } else {\n                    resolve();\n                }\n            }\n        }\n    } catch (e) {\n        app.log(e);\n        return resolve();\n    }\n})",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-06T18:13:53.979Z",
          "email": "parvez@yellowmessenger.com",
          "name": "preinspectionRequestInit",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac16",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    let data = app.context.steps['payment-link'].split('-$$-');\n    const userDetails = JSON.parse(data[1]);\n    if (app.source === 'facebook') {\n        app.executeFunction('crmApi', args = { data: userDetails, status: 'Closed', intentName: \"log-payment-link\" }).then(() => {\n            app.sendTextMessage('Please follow the below link').then(() => {\n                app.sendCards([\n                    {\n                        title: 'Renewal Payment link',\n                        text: '',\n                        actions: [\n                            {\n                                title: 'Pay now',\n                                url: data[2].replace(/%/g, '&')\n                            }\n                        ]\n                    },\n                    {\n                        title: 'Other Services',\n                        text: '',\n                        actions: [\n                            {\n                                title: 'Services',\n                                text: 'services'\n                            }\n                        ]\n                    },\n                ]).then(()=>{\n                    return resolve();\n                })\n            })\n        })\n    } else {\n        app.sendEvent({\n            code: \"load_pdf\",\n            data: {\n                url: data[2].replace(/%/g, '&'),\n            }\n        });\n        app.executeFunction('crmApi', args = { data: userDetails, status: 'Closed', intentName: \"log-payment-link\" }).then(() => {\n            app.triggerIntent('anything-else', {});\n            return;\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-31T17:35:57.402Z",
          "email": "parvez@yellowmessenger.com",
          "name": "logPaymentLink",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac17",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.validate(app.data.message).then((result) => {\n        if (!result && app.context.intent != 'calim-intimation') {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"email-validator\", {}, \"Please enter a valid email id\")\n            })\n        } else if (/^(([^<>()\\[\\]\\\\.,;:\\s@\"]+(\\.[^<>()\\[\\]\\\\.,;:\\s@\"]+)*)|(\".+\"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,}))$/g.test(result)) {\n            result = result.toLowerCase();\n            app.setContextParam('secondary-email', result);\n            app.pushData({ secondary_email: result }, app.context.intent)\n            return resolve();\n        }else if(result.toLowerCase() === 'noemailid'){\n            app.setContextParam('secondary-email', \"\");\n            return resolve();\n        } else {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"email-validator\", {}, \"Please enter a valid email id\")\n            })\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2018-12-19T14:55:46.727Z",
          "email": "parvez@yellowmessenger.com",
          "name": "secondaryEmailValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac18",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    let date = new Date().toLocaleString(\"en-US\", { hour12: false, timeZone: \"Asia/Calcutta\" });\n    let time = date.split(',')[1].trim();\n    let hour = time.split(':')[0];\n    app.log(hour, \"HOURS\");\n    let day = new Date(date).getDay();\n    if ((day == 0 || hour > 20 || hour < 9) && !app.UAT_ENV) {\n        app.sendTextMessage(\"Sorry, we won’t be able to process your request at the moment. Please try again on Mon – Sat (9 AM to 8 PM) for this query. Thank you for your patience.\");\n        app.clearContext();\n        app.triggerIntent(\"anything-else\", {});\n        return;\n    } else {\n        if (/^.*hindi.*$/ig.test(app.data.message)) {\n            app.memory.set('othersLanguage', 'hi').then(() => {\n                app.options.targetLanguage = 'hi';\n                app.pushData({ language: 'Hindi' }, app.context.intent);\n                app.triggerIntent(app.context.intent, {}, { 'select-language': 'hi' });\n                return;\n            })\n        } else {\n            app.memory.set('othersLanguage', 'en').then(() => {\n                app.options.targetLanguage = 'en';\n                app.pushData({ language: 'English' }, app.context.intent);\n                app.triggerIntent(app.context.intent, {}, { 'select-language': 'en' });\n                return;\n            })\n        }\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-02T08:00:13.017Z",
          "email": "parvez@yellowmessenger.com",
          "name": "othersInit",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac19",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    let array = ['policy-document', 'renewal-policy', 'claim-intimation', 'inspection'];\n    if (array.includes(app.context.intent) && app.source === 'facebook') {\n        app.clearContext();\n        app.sendTextMessage('Sorry, This facility is not available on facebook yet, but you can access it from the web.').then(() => {\n            app.sendTextMessage('Please follow the below link or you can access our other services.').then(()=>{\n                app.sendCards([\n                    {\n                        title:'Tara',\n                        text:'',\n                        actions:[\n                            {\n                                title:'Navigate',\n                                url:'https://yellow.chat/tata_aig/'\n                            }\n                        ]\n                    },\n                    {\n                        title:'Services',\n                        text:'',\n                        actions:[\n                            {\n                                title:'Show options',\n                                text:'services'\n                            }\n                        ]\n                    },\n                ]).then(()=>{\n                    return resolve();\n                })\n            });\n        });\n    } else {\n        app.memory.delete('othersLanguage');\n        app.options.targetLanguage = 'en';\n        resolve();\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-06T18:34:00.418Z",
          "email": "parvez@yellowmessenger.com",
          "name": "commonInit",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac1a",
          "code": "const askName = () => {\n    return app.sendQuickReplies({\n        title: app.renderMessage('policy-number', {}, \"Please tell me your policy number\"),\n        options: [\n            {\n                title: \"Don't have policy number\",\n                text: 'nopolicynumber'\n            }\n        ]\n    });;\n}\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    app.memory.get('userDetails').then(user => {\n        user = JSON.parse(user);\n        if (user.policy) {\n            app.sendQuickReplies({\n                title: app.renderMessage('policy-number', {}, \"Please tell me your policy number\"),\n                options: [\n                    {\n                        title: user.policy,\n                        text: user.policy\n                    },\n                    {\n                        title: \"Don't have policy number\",\n                        text: 'nopolicynumber'\n                    }\n                ]\n            });\n            return resolve();\n        } else {\n            askName()\n            return resolve();\n        }\n    }).catch(err => {\n        askName()\n        return resolve();\n    });\n\n}); ",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-22T08:28:39.481Z",
          "email": "parvez@yellowmessenger.com",
          "name": "othersPolicyNumberQF",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac1b",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    try {\n        app.validate(app.data.message).then((result) => {\n            if (!result) {\n                return resolve({\n                    success: false,\n                    question: app.renderMessage(\"policy-number\", {}, \"Please enter a 10 digit policy number\")\n                })\n            } else if (app.data.message === 'nopolicynumber') {\n                app.setContextParam('policy-number', result);\n                app.pushData({ \"policy_number\": result }, app.context.intent);\n                return resolve();\n            } else if (/^\\d{10}$/g.test(result)) {\n                app.setContextParam('policy-number', result);\n                app.executeFunction('updateCustomerInformation', args = { field: \"policy\", value: result });\n                app.pushData({ \"policy_number\": result }, app.context.intent);\n                return resolve();\n            } else {\n                return resolve({\n                    success: false,\n                    question: app.renderMessage(\"policy-number\", {}, \"Please enter a 10 digit policy number\")\n                })\n            }\n        })\n    } catch (err) {\n        app.log(err, \"ERROR\");\n        app.sendTextMessage(app.renderMessage('calim-error', {}, \"\"))\n        app.triggerIntent('anything-else', {});\n        return;\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-25T06:45:16.538Z",
          "email": "parvez@yellowmessenger.com",
          "name": "othersPolicyValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac1c",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const options = {\n        method: 'GET',\n        url: 'https://maps.googleapis.com/maps/api/geocode/json',\n        qs:\n        {\n            address: args.city,\n            key: 'AIzaSyBrojomjYgAZN_AdBq-Bk7xZTnZQ1eA7KU'\n        },\n        headers:\n        {\n            'Postman-Token': '2a9c0c07-4eaa-4b45-8f47-383c3dfd6b90',\n            'cache-control': 'no-cache'\n        }\n    };\n\n    app.request.request(options, function (error, response, body) {\n        if (error) {\n            app.log(error, \"ERror in geoCOrdinates\");\n            return resolve(false)\n        } else {\n            if (typeof body === 'string') {\n                body = JSON.parse(body);\n            }\n            if (body && body.results && body.results[0].geometry && body.results[0].geometry.location) {\n                body = body.results[0].geometry.location;\n                return resolve({ lat: body.lat, lon: body.lng });\n            } else {\n                return resolve(false)\n            }\n        }\n    });\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-01-24T08:56:45.846Z",
          "email": "parvez@yellowmessenger.com",
          "name": "googleNameToLatLon",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac1d",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    // Your logic goes here\n    app.memory.delete('othersLanguage');\n    let date = new Date().toLocaleString(\"en-US\", { hour12: false, timeZone: \"Asia/Calcutta\" });\n    let time = date.split(',')[1].trim();\n    let hour = time.split(':')[0];\n    app.log(hour, \"HOURS\");\n    let day = new Date(date).getDay();\n    if ((day == 0 || hour > 20 || hour < 8) && !app.UAT_ENV) {\n        app.sendTextMessage(\"Sorry, we won’t be able to process your request at the moment. Please try again on Mon – Sat (8 AM to 8 PM) for this query. Thank you for your patience.\");\n        app.clearContext();\n        app.triggerIntent(\"anything-else\", {});\n        return;\n    } else {\n        app.options.targetLanguage = 'en';\n        const value = app.data.message;\n        if (/^.*(travel).*$/ig.test(value)) {\n            app.setStep('type', 'travel').then(() => {\n                app.pushData({ type: 'travle' }, app.context.intent);\n                return resolve();\n            });\n        } else if (/^.*(health).*$/ig.test(value)) {\n            app.setStep('type', 'health').then(() => {\n                app.pushData({ type: 'health' }, app.context.intent);\n                return resolve();\n            });\n        } else if (/^.*(motor).*$/ig.test(value)) {\n            app.setStep('type', 'car').then(() => {\n                app.pushData({ type: 'car' }, app.context.intent);\n                return resolve();\n            });\n        } else if (/^.*(accident).*$/ig.test(value)) {\n            app.setStep('type', 'accident').then(() => {\n                app.pushData({ type: 'accident' }, app.context.intent);\n                return resolve();\n            });\n        } else {\n            return resolve();\n        }\n    }\n\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-02T08:30:00.067Z",
          "email": "parvez@yellowmessenger.com",
          "name": "buyOnlineInit",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac1e",
          "code": "const claimTableName = \"claim_intimation_lead_id\";\nconst errorMessage = (data, requestBody, responseBody, error, steps, elapsedTime) => {\n    data.leadId = data.leadId ? data.leadId : \"API Timed Out or Error\";\n    data.assignedTo = steps.motorType === 'Commercial' ? \"hshanke\" : \"dgavali\";\n    app.executeFunction('crmApi', args = { data: data, status: 'Open', intentName: \"claim-intimation\" }).then((ticket) => {\n        app.pushData({ transaction: 'Failed', message: data.leadId, crm_ticket: ticket }, app.context.intent).then(() => {\n            app.memory.delete(claimTableName);\n        });\n        app.sendTextMessage(app.renderMessage('claim-error-success', { ticket: ticket }, \"\")).then(() => {\n            app.executeFunction('apiResponseDatabase', args = { request: requestBody, response: responseBody, error: error, tableName: \"claim_intimation_api_database\", \"type\": \"Claim Intimation\", \"elapsedTime\": elapsedTime, steps: steps });\n            app.executeFunction('sendApiFailureEmail', args = { request: requestBody, response: responseBody, error: error, tableName: \"claim_intimation_api_database\", \"type\": \"Claim Intimation\", \"elapsedTime\": elapsedTime, \"ticketNumber\": ticket, \"intentName\": 'claim-intimation' })\n            app.triggerIntent('anything-else', {});\n            return;\n        });\n    });\n\n}\n\nconst successErrorMessage = (data, requestBody, responseBody, error, steps, elapsedTime) => {\n    return new Promise(resolve => {\n        app.executeFunction('apiResponseDatabase', args = { request: requestBody, response: responseBody, error: error, tableName: \"claim_intimation_api_database\", \"type\": \"Claim Intimation\", \"elapsedTime\": elapsedTime })\n        app.executeFunction('crmApi', args = { data: data, status: 'Closed', intentName: \"claim-intimation\" }).then((ticketNumber) => {\n            app.pushData({ transaction: 'success', message: data.leadId ? data.leadId : data.claimNo, crm_ticket: ticketNumber }, app.context.intent).then(() => {\n                app.sendTextMessage(app.renderMessage(\"ticket-number\", { ticket: ticketNumber }, \"\")).then(() => {\n                    app.memory.delete(claimTableName);\n                    app.triggerIntent('anything-else', {});\n                    return;\n                })\n            })\n        })\n    });\n}\n\nreturn new Promise(resolve => {\n    try {\n        // app.sendTextMessage('in new Flow')\n        const steps = app.context.steps;\n        // app.sendTextMessage(JSON.stringify(steps));\n        let source = 'TATA-AIG';\n        let medium = 'CHATBOT';\n        let email = steps['email'] === 'noemailid' ? \"\" : steps['email'];\n        let lossTime = new Date(steps['accident-date-time']).toLocaleTimeString().split(':');\n        lossTime = lossTime[0] + \":\" + lossTime[1]\n        let lossDate = steps['date-time'].split(' ')[0];\n        let curDate = new Date().toLocaleDateString().split('-');\n        curDate = `${curDate[2]}/${curDate[1]}/${curDate[0]}`\n        let curTime = new Date();\n        curTime = new Date(curTime.getTime() + 330 * 60000).toLocaleTimeString().split(':');\n        curTime = curTime[0] + \":\" + curTime[1];\n        let insuredName = steps['insured-person'] === 'yes' ? '' : steps['customer-name'];\n        let insuredMobile = steps['insured-person'] === 'yes' ? steps['mobile'] : steps['insured-mobile'];\n        let insured = steps['insured-person'] === 'yes' ? 'Insured' : '';\n        let pincode = steps['claim-city'].split('$')[3];\n        let settlingOffice = steps['claim-city'].split('$')[1];\n        let curCity = steps['city-name'] ? steps['city-name'] : \"\";\n        let garage = steps['garage-or-not'] === 'With Insured' ? curCity + ', ' + steps['garage-or-not'] : steps['garage-or-not'];\n        let lossLocation = `${curCity}, ${steps['district-name'] ? steps['district-name'] : \"\"}, ${steps['state-name'] ? steps['state-name'] : \"\"}`;\n        if (app.UAT_ENV) {\n            source = 0;\n            medium = 0;\n        }\n        //If location is garage or other\n        if (steps['garage-or-not'] === 'garage') {\n            garage = `${steps.garage}, ${steps['cur-city-name']}, ${steps['cur-district-name']}, ${steps['cur-state-name']}`;\n        } else if (steps['garage-or-not'] === 'With Insured') {\n            garage = `${steps['cur-landmark']}, ${steps['cur-city-name']}, ${steps['cur-district-name']}, ${steps['cur-state-name']}`;\n        }\n        let userData = {\n            username: steps['customer-name'],\n            mobileNo: steps['mobile'],\n            email: email,\n            policyNo: steps['policy-number'],\n            leadId: \"\",\n            claimNo: \"\",\n            callerRelation: steps['insured']\n        }\n        let claimType = { \"OD\": \"24971\", \"stolen\": \"9948\", \"parked\": \"24971\", \"Key\": \"24873\", \"tyre\": \"24879\" };\n        let driverName = steps['driver-name'] === 'Vehicle was parked' ? \"\" : steps['driver-name'];\n        let licenseNo = steps['license-no'] === 'Vehicle was parked' ? \"\" : steps['license-no'];\n        let parked = steps['vehicleParked'] ? steps['vehicleParked'] : \"No\"\n\n        //API BODY \n        let options = {\n            method: 'POST',\n            url: app.claimUrl,\n            qs: { wsdl: '' },\n            timeout: app.timeOut,\n            headers:\n            {\n                'Postman-Token': 'e902a49d-0b14-4212-9140-f9aefd9a6fc2',\n                'cache-control': 'no-cache',\n                'Content-Type': 'text/xml'\n            },\n            body: `\n<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:mot=\"http://stub.unotechsoft.com/wsdl/MotorClaimService/\" xmlns:cla=\"http://schemas.datacontract.org/2004/07/ClaimEntities\" xmlns:arr=\"http://schemas.microsoft.com/2003/10/Serialization/Arrays\">\n   <soapenv:Header/>\n   <soapenv:Body>\n      <mot:claimServiceRegisterClaim>\n         <mot:source>${source}</mot:source>\n         <mot:medium>${medium}</mot:medium>\n         <mot:campaign>${medium}</mot:campaign>\n         <mot:strServiceToken></mot:strServiceToken>\n         <mot:PolicyNumber>${steps['policy-number']}</mot:PolicyNumber>\n         <mot:LossDate>${lossDate}</mot:LossDate>\n         <mot:IntDate>${curDate}</mot:IntDate>\n         <mot:LossTime>${lossTime}</mot:LossTime>\n         <mot:IntTime>${curTime}</mot:IntTime>\n         <mot:NOLCode>${claimType[steps['claim-type']]}</mot:NOLCode>\n         <mot:LossDescCode>999</mot:LossDescCode>\n         <mot:LossDesc>${steps['description']}</mot:LossDesc>\n         <mot:PinCode>${pincode}</mot:PinCode>\n         <mot:ContactNo>${insuredMobile}</mot:ContactNo>\n         <mot:IsClaimantInsured>Yes</mot:IsClaimantInsured>\n         <mot:DriverName>${driverName}</mot:DriverName>\n         <mot:LicenseNo>${licenseNo}</mot:LicenseNo>\n         <mot:SettlingOffice>${settlingOffice.toUpperCase()}</mot:SettlingOffice>\n         <mot:ClaimType>${steps['claim-type'] === 'parked' ? 'OD' : steps['claim-type']}</mot:ClaimType>\n         <mot:DamageAddlDtls></mot:DamageAddlDtls>\n         <mot:WasVehicleParked>${parked}</mot:WasVehicleParked>\n         <mot:PolicyNotifnFIR>FIR11</mot:PolicyNotifnFIR>\n         <mot:CallerType>${insured}</mot:CallerType>\n         <mot:NoticedBy></mot:NoticedBy>\n         <mot:CallerInformedAbtClaimDoc>Yes</mot:CallerInformedAbtClaimDoc>\n         <mot:TATInformedtoCustomer>Yes</mot:TATInformedtoCustomer>\n         <mot:CallerInformedSurveyorWillContact>Naa</mot:CallerInformedSurveyorWillContact>\n         <mot:EmailID>${email}</mot:EmailID>\n         <mot:CallerName>${steps['customer-name']}</mot:CallerName>\n         <mot:CallerContactNo>${insuredMobile}</mot:CallerContactNo>\n         <mot:GarageDetails>${garage}</mot:GarageDetails>\n\t\t <mot:Landmark>${steps['loss-landmark']}</mot:Landmark>        \n\t\t <mot:AddOfAccident>${lossLocation}</mot:AddOfAccident> \n         <mot:SARMLRNo></mot:SARMLRNo>\n         <mot:AddInfo></mot:AddInfo>\n         <mot:CertNo></mot:CertNo>\n         <mot:CauseOfLossCode>${claimType[steps['claim-type']]}</mot:CauseOfLossCode>\n         <mot:ClaimStatus>Open</mot:ClaimStatus>\n         <mot:AnatCode></mot:AnatCode>\n         <mot:InjuryCode></mot:InjuryCode>\n         <mot:UserId>CHAT BOT</mot:UserId>\n         <mot:lstIndianCurrencyRiskDetails>\n            <!--Zero or more repetitions:-->\n            <cla:GDtRiskDetails_INR>\n               <cla:RowIndex></cla:RowIndex>\n               <cla:ACCOUNT_LINE></cla:ACCOUNT_LINE>\n               <cla:Claimable_Amount></cla:Claimable_Amount>\n               <cla:MemberID></cla:MemberID>\n               <cla:NUM_LOCATION_CD></cla:NUM_LOCATION_CD>\n               <cla:Num_Assessed_Amount></cla:Num_Assessed_Amount>\n               <cla:Num_Balance_SI></cla:Num_Balance_SI>\n               <cla:Num_Claim_Amount></cla:Num_Claim_Amount>\n               <cla:Num_Cover_Code></cla:Num_Cover_Code>\n               <cla:Num_Cubic_Capacity></cla:Num_Cubic_Capacity>\n               <cla:Num_SI></cla:Num_SI>\n               <cla:Num_Serial></cla:Num_Serial>\n               <cla:Num_Voluntary_Excess></cla:Num_Voluntary_Excess>\n               <cla:Policy_Risk_Serial></cla:Policy_Risk_Serial>\n               <cla:Risk_Detail_Serial></cla:Risk_Detail_Serial>\n               <cla:STATUS></cla:STATUS>\n               <cla:Txt_Cover_Code></cla:Txt_Cover_Code>\n               <cla:Txt_Risk_Element></cla:Txt_Risk_Element>\n               <cla:Txt_Risk_Element_Type></cla:Txt_Risk_Element_Type>\n               <cla:UniqueCode></cla:UniqueCode>\n            </cla:GDtRiskDetails_INR>\n         </mot:lstIndianCurrencyRiskDetails>\n         <mot:dicLVWFParams>\n            <!--Zero or more repetitions:-->\n           <arr:KeyValueOfstringstring>\n                    <arr:Key>KeyDms</arr:Key>\n                    <arr:Value>192.168.140.97:8080/dms.TAGIC/initiatelogin.do?</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>SLPageName</arr:Key>\n                    <arr:Value>ScrClm_ClaimRegistration</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>ConfiguratorUrl</arr:Key>\n                    <arr:Value>http://localhost/Configurator</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>CURRENT_STATE</arr:Key>\n                    <arr:Value>START_REGISTRATION</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>OTHER_STATE_INFO</arr:Key>\n                    <arr:Value />\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>WORKFLOW_NAME</arr:Key>\n                    <arr:Value>MotorODWorkflow</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>LOB</arr:Key>\n                    <arr:Value>D000020</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>PROCESS_NAME</arr:Key>\n                    <arr:Value>35</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>GUID_WORKFLOW</arr:Key>\n                    <arr:Value>6a7140e4-c910-44c1-8cae-f55ae9166d72</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>LINK_ID</arr:Key>\n                    <arr:Value>0</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>SIU</arr:Key>\n                    <arr:Value />\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>KYC</arr:Key>\n                    <arr:Value>KYC</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>AML</arr:Key>\n                    <arr:Value>Y</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>APPROVALSTATUS</arr:Key>\n                    <arr:Value>0</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>CURRENT_OUTSTANDING</arr:Key>\n                    <arr:Value>1</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>ISCLAIMCANCELLED</arr:Key>\n                    <arr:Value>N</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>ISCLAIMClOSED</arr:Key>\n                    <arr:Value>N</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>AppUserID</arr:Key>\n                    <arr:Value>1003</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>UserRole</arr:Key>\n                    <arr:Value>ADMIN</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>AppSessionID</arr:Key>\n                    <arr:Value>SL-CONF-100000000432188</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>SessionIDDMS</arr:Key>\n                    <arr:Value>100000000432188</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>SystemMailSender</arr:Key>\n                    <arr:Value>abcinsuranceonline@gmail.com</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>SessionIsNothing</arr:Key>\n                    <arr:Value>False</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>ErrorLogCheck</arr:Key>\n                    <arr:Value>0</arr:Value>\n                </arr:KeyValueOfstringstring>\n                <arr:KeyValueOfstringstring>\n                    <arr:Key>AssemblyVersionCheck</arr:Key>\n                    <arr:Value>0</arr:Value>\n                </arr:KeyValueOfstringstring>\n         </mot:dicLVWFParams>\n      </mot:claimServiceRegisterClaim>\n   </soapenv:Body>\n</soapenv:Envelope>\n\n        `\n        };\n        const startTime = new Date();\n        // app.sendTextMessage('making request')\n        app.request.request(options, function (err, response, body) {\n            app.elapsedTime(startTime).then((elapsedTime) => {\n                if (err || response.statusCode !== 200) {\n                    errorMessage(userData, options, response, err, steps, elapsedTime);\n                    return resolve();\n                } else {\n                    let result = JSON.parse(app.xmlToJSON.toJson(body));\n                    if (result['soap:Envelope']['soap:Body']['claimServiceRegisterClaimResponse']['ClaimServiceRegisterClaimResult']) {\n                        const details = result['soap:Envelope']['soap:Body']['claimServiceRegisterClaimResponse']['ClaimServiceRegisterClaimResult'];\n                        if ((details && details[\"ns2:Message\"] && details[\"ns2:Message\"][\"ns2:MessageType\"] && details[\"ns2:Message\"][\"ns2:MessageType\"] == \"ERROR\") ||\n                            (details && details[\"ns2:Message\"] && details[\"ns2:Message\"]['ns2:Message'] && details[\"ns2:Message\"]['ns2:Message'] === \"Problem in Selecting Risk Details\")) {\n                            if (details[\"ns2:Message\"][\"ns2:Message\"] && details[\"ns2:Message\"][\"ns2:Message\"] !== 'Problem in Selecting Risk Details') {\n                                app.sendTextMessage(details[\"ns2:Message\"][\"ns2:Message\"]).then(function () {\n                                    //Conversation is finshed but CRM ticket is open\n                                    userData.leadId = details[\"ns2:Message\"][\"ns2:Message\"]\n                                    errorMessage(userData, options, response, err, steps, elapsedTime).then(() => {\n                                        return resolve()\n                                    })\n                                });\n                            }\n                            else {\n                                errorMessage(userData, options, response, err, steps, elapsedTime);\n                                return resolve();\n                            }\n                        } else if (details['ns2:ClaimDetails'] && details['ns2:ClaimDetails']['ns2:GDTClaimDetails']['ns2:ClaimNo'] && details['ns2:ClaimDetails']['ns2:GDTClaimDetails']['ns2:ClaimNo'].trim() && JSON.stringify(details['ns2:ClaimDetails']['ns2:GDTClaimDetails']['ns2:ClaimNo']) != \"\") {\n                            let claim_no = details['ns2:ClaimDetails']['ns2:GDTClaimDetails']['ns2:ClaimNo'].toString();\n                            userData.claimNo = details['ns2:ClaimDetails']['ns2:GDTClaimDetails']['ns2:ClaimNo'];\n                            app.sendTextMessage(app.renderMessage('claim-thankyou', { details: { claim: claim_no } }, `Thank you. We have taken your claim request. Your claim number is <strong>${claim_no}</strong>.`)).then(() => {\n                                app.sendTextMessage(app.renderMessage('claim-documents', {}, `Our Claim officials will contact you within the next 48 workings hours. Request you to kindly submit the following documents (self-attested) during the survey:\n                                                    1. Claim form\n                                                    2. Driving license copy\n                                                    3. RC copy\n                                                    4. FIR copy (if any)\n\n                                                P.S- Additional Documents maybe asked for, as per the merit of your claim. It will be informed to you by our claim officials.`));\n                            }).then(function () {\n                                successErrorMessage(userData, options, response, err, steps, elapsedTime).then(() => {\n                                    return resolve();\n                                })\n                            });\n                        }\n                    } else {\n                        errorMessage(userData, options, response, err, steps, elapsedTime);\n                        return resolve();\n                    }\n                }\n            });\n        });\n    } catch (err) {\n        app.log(err, \"THIS IS ERROR\");\n        errorMessage(userData, requestBody, '', err, '', '');\n        return resolve();\n    }\n\n})",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-06T13:04:08.468Z",
          "email": "parvez@yellowmessenger.com",
          "name": "newClaim",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac1f",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    if (app.source === 'facebook') {\n\n    } else {\n        resolve();\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-06T18:18:51.398Z",
          "email": "parvez@yellowmessenger.com",
          "name": "greetingPrompt",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac20",
          "code": "const motorProductCode = [3121, 3122, 3124];\nreturn new Promise(resolve => {\n    // Your logic goes here\n    // Test Policy Numbber  0155015498 0177551431 0235031324\n    let result = app.data.message;\n    if (/^[012]\\d{9}$/g.test(result)) {\n        app.setContextParam('policy-number', result);\n        app.executeFunction('updateCustomerInformation', args = { field: \"policy\", value: result });\n        app.executeFunction('getMobileNumber', args = { \"policyNumber\": result }).then((mobileNumbers) => {\n            app.log(mobileNumbers, \"This are mobile numbers\")\n            if ((mobileNumbers.mobile1 === \"\" && mobileNumbers.mobile2 === \"\" && false) || !mobileNumbers) {\n                app.sendTextMessage(app.renderMessage('wrong-policy', {}, \"The poilcy you have entered is not available in TATA AIG please verify it and try agian.\")).then(() => {\n                    app.pushData({ policy_number: result, transaction: 'Mobile numbers not found' }, app.context.intent).then(() => {\n                        app.memory.delete('nil_endorsement_leads_id');\n                        app.triggerIntent('anything-else');\n                        return;\n                    });\n                });\n            } else {\n                app.executeFunction('proposalNumberApi').then((productCode) => {\n                    if (motorProductCode.indexOf(Number(productCode)) > -1) {\n                        app.pushData({ \"policy_number\": result }, app.context.intent);\n                        app.executeFunction('updateCustomerInformation', args = { field: \"mobile\", value: mobileNumbers });\n                        return resolve();\n                    } else {\n                        app.pushData({ \"policy_number\": result }, app.context.intent);\n                        app.setStep('services', 'Non Motor Policy').then(() => {\n                            return resolve();\n                        });\n                    }\n                });\n            }\n        })\n    } else {\n        return resolve({\n            success: false,\n            question: app.renderMessage(\"policy-number\", {}, \"Please enter a 10 digit policy number\")\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-11T05:04:07.326Z",
          "email": "parvez@yellowmessenger.com",
          "name": "nilPolicyValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac21",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const options = {\n        url: app.proposalUrl,\n        method: \"POST\",\n        body: `\n            <soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:dbs=\"http://stub.unotechsoft.com/wsdl/DBService/\">\n   <soapenv:Header/>\n   <soapenv:Body>\n      <dbs:getRenewalData>\n         <dbs:Source>0</dbs:Source>\n         <dbs:Medium>0</dbs:Medium>\n         <dbs:Campaign>0</dbs:Campaign>\n         <dbs:AuthenticationToken></dbs:AuthenticationToken>\n         <dbs:PolicyNo>${app.data.message}</dbs:PolicyNo>\n      </dbs:getRenewalData>\n   </soapenv:Body>\n</soapenv:Envelope>\n        `\n    }\n    const startTime = new Date();\n    app.request.request(options, (err, res, body) => {\n        app.elapsedTime(startTime).then(elapsedTime => {\n            app.executeFunction('apiResponseDatabase', args = { request: options, response: body, error: err, tableName: \"proposal_api_database\", \"type\": \"Proposal number\", \"elapsedTime\": elapsedTime });\n            if (err || !body) {\n                app.sendTextMessage(app.renderMessage('proposal-error', {}, '')).then(() => {\n                    app.triggerIntetn('anything-else', {});\n                    return;\n                })\n            } else {\n                try {\n                    body = app.xmlToJSON.toJson(body);\n                    if (typeof body === 'string') {\n                        body = JSON.parse(body);\n                    }\n                    if (body['soap:Envelope'] && body['soap:Envelope']['soap:Body'] && body['soap:Envelope']['soap:Body']['ns2:getRenewalDataResponse']\n                        && body['soap:Envelope']['soap:Body']['ns2:getRenewalDataResponse']['ns2:GetRenewalDataResult']\n                        && body['soap:Envelope']['soap:Body']['ns2:getRenewalDataResponse']['ns2:GetRenewalDataResult']['PolicyOutput'] === \"SUCCESSFUL\") {\n                        app.log(body['soap:Envelope']['soap:Body']['ns2:getRenewalDataResponse']['ns2:GetRenewalDataResult'], \"logAPI\")\n                        app.setStep('proposalNumber', body['soap:Envelope']['soap:Body']['ns2:getRenewalDataResponse']['ns2:GetRenewalDataResult']['ProposalNo']).then(() => {\n                            let productCode =  body['soap:Envelope']['soap:Body']['ns2:getRenewalDataResponse']['ns2:GetRenewalDataResult']['ProductCode'];\n                            app.setStep('productCode', productCode);\n                            return resolve(productCode);\n                        });\n                    } else {\n                        app.sendTextMessage(app.renderMessage('wrong-policy', {}, '')).then(() => {\n                            app.pushData({ policy_number: result, transaction: 'Mobile numbers not found' }, app.context.intent).then(() => {\n                                app.memory.delete('');\n                                app.triggerIntent('anything-else');\n                                return;\n                            });\n                        });\n                    }\n                } catch (err) {\n                    app.sendTextMessage('Oops! something went wrong please try again.').then(() => {\n                        app.pushData({ policy_number: result, transaction: 'Failed' }, app.context.intent).then(() => {\n                            app.memory.delete('');\n                            app.triggerIntent('anything-else');\n                            return;\n                        });\n                    });\n                }\n            }\n        });\n    });\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-10T06:37:35.549Z",
          "email": "parvez@yellowmessenger.com",
          "name": "proposalNumberApi",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac22",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.validate(app.data.message).then((result) => {\n        if (!result) {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"email-validator\", {}, \"Please enter a valid email id\")\n            })\n        } else if (/^(([^<>()\\[\\]\\\\.,;:\\s@\"]+(\\.[^<>()\\[\\]\\\\.,;:\\s@\"]+)*)|(\".+\"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,}))$/g.test(result)) {\n            result = result.toLowerCase();\n            app.pushData({ email_id : result }, app.context.intent)\n            return resolve();\n        } else {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"email-validator\", {}, \"Please enter a valid email id\")\n            })\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-09T18:44:56.954Z",
          "email": "parvez@yellowmessenger.com",
          "name": "nilEmailValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac23",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    app.validate(app.data.message).then((result) => {\n        if (!result) {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"email-validator\", {}, \"Please enter a valid email id\")\n            })\n        } else if (/^(([^<>()\\[\\]\\\\.,;:\\s@\"]+(\\.[^<>()\\[\\]\\\\.,;:\\s@\"]+)*)|(\".+\"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,}))$/g.test(result)) {\n            result = result.toLowerCase();\n            app.pushData({ alt_email : result }, app.context.intent)\n            return resolve();\n        } else {\n            return resolve({\n                success: false,\n                question: app.renderMessage(\"email-validator\", {}, \"Please enter a valid email id\")\n            })\n        }\n    })\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-09T18:45:20.419Z",
          "email": "parvez@yellowmessenger.com",
          "name": "nilAltEmailValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac24",
          "code": "const motorProductCode = [3121, 3122, 3124];\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    const productCode = Number(app.context.steps['productCode']);\n    let options = [\n        {\n            title: 'Email ID',\n            text: 'change email id'\n        },\n        {\n            title: 'Alternate Email ID',\n            text: 'change Alternate Email ID'\n        },\n        {\n            title: 'Marital Status',\n            text: 'change Marital Status'\n        },\n        {\n            title: 'Occupation',\n            text: 'change Occupation'\n        },\n        {\n            title: 'Contact number',\n            text: 'change Contact number'\n        },\n        {\n            title: 'Change Address',\n            text: 'change address'\n        },\n        {\n            title: 'Aadhaar Card',\n            text: 'change Aadhaar number'\n        },\n        {\n            title: 'Pan Card',\n            text: 'change pancard'\n        },\n        {\n            title:'Change Title',\n            text:'change title'\n        }\n    ];\n    if (productCode !== NaN && motorProductCode.includes(productCode)) {\n        options.push({\n            title: 'Vehicle Number',\n            text: 'change Vehicle Number'\n        })\n    }\n    app.sendQuickReplies({\n        title: \"Kindly select the details that needs to be modified.\",\n        multiSelect: true,\n        options:options\n    }).catch(err=>{\n        app.sendTextMessage('catch')\n    })\n    return resolve();\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-14T09:37:16.988Z",
          "email": "parvez@yellowmessenger.com",
          "name": "servicesQF",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac25",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    let array = ['change email id', 'change alternate email id', 'change marital status', 'change occupation', 'change contact number', 'change aadhaar number', 'change pancard', 'change title', 'change vehicle number', 'change address'];\n    let messages = app.data.message.toLowerCase().split(',');\n    let counter = 0;\n    app._.forEach(messages, function (value) {\n        if (value.split(' ').join('-') === 'change-address') {\n            app.setStep('address', \"true\");\n            app.setStep('change-pincode', undefined).then(()=>{\n                app.setStep('change-address', undefined);\n                counter++;\n            });\n        } else {\n            value = value.split(' ').join('-');\n            app.setStep(value, undefined);\n            counter++;\n        }\n    });\n    if (counter > 0) {\n        app.pushData({ changes_in: app.data.message }, app.context.intent);\n        return resolve();\n    } else {\n        let options = [];\n        app._.forEach(array, function (value) {\n            options.push({\n                title: value[0].toUpperCase() + value.slice(1)\n            });\n        });\n        app.sendQuickReplies({\n            title: 'Sorry I can only help you with the following services',\n            options: options\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-25T09:13:03.458Z",
          "email": "parvez@yellowmessenger.com",
          "name": "servicesValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac26",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const arry = ['single', 'married', 'unknown', 'Widowed', 'Divorced'];\n    const value = app.data.message.toLowerCase();\n    if (arry.indexOf(value) > -1) {\n        app.pushData({ marital_status: value }, app.context.intent);\n        return resolve();\n    } else {\n        app.sendQuickReplies({\n            title: 'Please let me know if you are married or single.',\n            options: [\n                {\n                    title: 'Single'\n                },\n                {\n                    title: 'Married'\n                },\n                {\n                    title: 'Unknown'\n                },\n                {\n                    title: 'Widowed'\n                },\n                {\n                    title: 'Divorced'\n                }\n            ]\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-09T21:08:43.552Z",
          "email": "parvez@yellowmessenger.com",
          "name": "maritalStatusValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac27",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const value = app.data.message;\n    if (value && value.startsWith('$-')) {\n        app.pushData({ occupation: value.replace('$-', '') }, app.context.intent);\n        app.setStep('change-occupation', value.replace('$-', '')).then(() => {\n            return resolve();\n        });\n    } else {\n        let es_query = {\n            query: {\n                match: {\n                    \"name\": value\n                }\n            }\n        };\n        app.executeFunction('searchQuery', { table: 'occupation', es_query: es_query }).then((result) => {\n            if (!result) {\n                return resolve({\n                    success: false,\n                    question: 'Please choose your occupation from the suggestions'\n                });\n            } else {\n                app.pushData({ occupation: result.name }, app.context.intent);\n                app.setStep('change-occupation', result.name).then(() => {\n                    return resolve();\n                });\n            }\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-09T19:38:30.798Z",
          "email": "parvez@yellowmessenger.com",
          "name": "occupationValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac28",
          "code": "return new Promise(function (resolve) {\n    if (app.term) {\n        app.dataStore.search({\n            table: \"occupation\",\n            body: {\n                \"query\": {\n                    \"regexp\": { \"name\": app.term.toLowerCase() + \".*\" }\n                }\n            }\n        }).then((result) => {\n            resolve(app._.map(result.hits.hits, function (hit) {\n                return [hit._source.name, \"$-\" + hit._source.name];\n            }))\n\n        })\n    } else { resolve([]) }\n})",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-09T19:35:52.923Z",
          "email": "parvez@yellowmessenger.com",
          "name": "occupationAutoComplete",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac29",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    let array = ['policy-document', 'renewal-policy', 'claim-intimation', 'inspection', 'nil-endorsement'];\n    if (array.includes(app.context.intent) && app.source === 'facebook') {\n        app.clearContext();\n        app.sendTextMessage('Sorry, This facility is not available on facebook yet, but you can access it from the web.').then(() => {\n            app.sendTextMessage('Please follow the below link or you can access our other services.').then(() => {\n                app.sendCards([\n                    {\n                        title: 'Tara',\n                        text: '',\n                        actions: [\n                            {\n                                title: 'Navigate',\n                                url: 'https://yellow.chat/tata_aig/'\n                            }\n                        ]\n                    },\n                    {\n                        title: 'Services',\n                        text: '',\n                        actions: [\n                            {\n                                title: 'Show options',\n                                text: 'services'\n                            }\n                        ]\n                    },\n                ]).then(() => {\n                    return resolve();\n                })\n            });\n        });\n    } else {\n        let array = ['change email id', 'change alternate email id', 'change marital status', 'change occupation', 'change contact number', 'change aadhaar number', 'change pancard', 'change title', 'change vehicle number', 'change address', 'change pincode'];\n        app.memory.delete('othersLanguage');\n        app.options.targetLanguage = 'en';\n        app._.forEach(array, function(step){\n            app.setStep(step.split(' ').join('-'), \"\");\n        });\n        return resolve();\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-14T09:38:26.832Z",
          "email": "parvez@yellowmessenger.com",
          "name": "nilEndoresementInit",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac2a",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const value = app.data.message;\n    if (value.length) {\n        app.pushData({'pan_card':value}, app.context.intent);\n        return resolve();\n    } else {\n        return resolve({\n            success: false,\n            question: 'Please enter a valid pan card number'\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-09T21:14:08.776Z",
          "email": "parvez@yellowmessenger.com",
          "name": "nilPanValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac2b",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const value = app.data.message.replace(/[^0-9]/g, '');\n    if(value.length === 12){\n        app.pushData({'aadhaar_card':value}, app.context.intent);\n        return resolve();\n    }else{\n        return resolve({\n            success:false,\n            question:'Please enter a valid aadhaar card number'\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-09T21:11:31.561Z",
          "email": "parvez@yellowmessenger.com",
          "name": "nilaadhaarValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac2c",
          "code": "const nonMotorPolicy = (crmData) => {\n    app.executeFunction('crmApi', args = { data: crmData, status: 'Open', intentName: \"nil-endorsement\" }).then((ticket) => {\n        app.sendTextMessage('Thank you for availing our services, your request have been submitted successfully. Please note down the ticket number ' + ticket + 'for future refrence.').then(() => {\n            app.memory.delete('nil_endorsement_leads_id');\n            app.triggerIntent('anything-else', {});\n            return;\n        });\n    });\n};\nreturn new Promise(resolve => {\n    // Your logic goes here\n    const value = app.data.message.split(' ');\n    const steps = app.context.steps;\n    let crmData = {\n        username: steps['cust-name'],\n        mobileNo: steps['mobile-number'],\n        email: steps['email-id'],\n        policyNo: steps['policy-number'],\n        leadId: \"\",\n        claimNo: \"\",\n        callerRelation: \"\"\n    };\n\n    if (value.length >= 4) {\n        if (app.context.steps.services === 'Non Motor Policy') {\n            app.pushData({ remark: app.data.message, changes_in: 'Non Motor Policy' }, app.context.intent).then(() => {\n                crmData.leadId = app.data.message;\n                nonMotorPolicy(crmData);\n            });\n        } else {\n            app.pushData({ remark: app.data.message }, app.context.intent);\n            return resolve();\n        }\n    } else {\n        return resolve({\n            success: false,\n            question: 'Please enter more than 4 words.'\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-11T05:31:17.726Z",
          "email": "parvez@yellowmessenger.com",
          "name": "remarkValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac2d",
          "code": "const askName = () => {\n    return app.sendTextMessage('Can you please provide me your policy number');\n}\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    app.memory.get('userDetails').then(user => {\n        user = JSON.parse(user);\n        if (user.policy) {\n            app.sendQuickReplies({\n                title: \"Can you please provide me your policy number\",\n                options: [{\n                    title: user.policy,\n                    text: user.policy\n                }]\n            });\n            return resolve();\n        } else {\n            askName()\n            return resolve();\n        }\n    }).catch(err => {\n        askName()\n        return resolve();\n    });\n\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-10T06:49:35.985Z",
          "email": "parvez@yellowmessenger.com",
          "name": "nilPolicyQf",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac2e",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const value = app.data.message.replace(/[^a-zA-Z0-9]/g, '');\n    if(value.length > 6){\n        app.setStep('change-vehicle-number', value);\n        app.pushData({change_vehicle_number : value}, app.context.intent);\n        return resolve();\n    }else{\n        return resolve({\n            success:false,\n            question:'Please enter a valid vehicle number'\n        })\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-10T07:00:36.429Z",
          "email": "parvez@yellowmessenger.com",
          "name": "nilVehicleValidator",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac2f",
          "code": "//TO DO if the API gives Failed response\nconst successMessage = (crmData, ProposalNo, jsonRequest, rawRequest, err, response, status, elapsedTime) => {\n    app.executeFunction('crmApi', { data: crmData, status: status, intentName: \"nil-endorsement\" }).then(ticketNumber => {\n        app.pushData({ proposal_number: ProposalNo, transaction: 'Success', crm_ticket: ticketNumber }, app.context.intent).then(() => {\n            app.sendTextMessage(app.renderMessage('nil-response', { data: { no: ticketNumber } }, '')).then(() => {\n                app.memory.delete('nil_endorsement_leads_id');\n                app.triggerIntent('anything-else', {});\n                return;\n            });\n        });\n    });\n}\n\nconst errorMessage = (crmData, jsonRequest, rawRequest, err, response, status, elapsedTime) => {\n    app.executeFunction('crmApi', { data: crmData, status: status, intentName: \"nil-endorsement\" }).then(ticketNumber => {\n        app.pushData({ transaction: 'Failed', crm_ticket: ticketNumber }, app.context.intent).then(() => {\n            app.sendTextMessage(app.renderMessage('nil-response', { data: { no: ticketNumber } }, '')).then(() => {\n                app.memory.delete('nil_endorsement_leads_id');\n                app.triggerIntent('anything-else', {});\n                return;\n            });\n        });\n    });\n};\n\nreturn new Promise(resolve => {\n    // Your logic goes here\n    let crmData = args.crmData;\n    const options = {\n        body: args.body,\n        url: app.nilUrl,\n        method: 'POST',\n        timeout: 50000\n    };\n    const startTime = new Date();\n    app.soap.createClient(app.nilUrl + '?wsdl', function (err, client) {\n        client.setEndpoint(app.nilUrl);\n        app.sendTextMessage('Please wait this can take upto 2 minutes..').then(() => {\n            app.elapsedTime(startTime).then((elapsedTime) => {\n                client.webServiceNilEndorsement(args.body, function (err, res, rawResponse, soapHeader, rawRequest) {\n                    app.executeFunction('apiResponseDatabase', args = { request: args.body, response: res, error: err, tableName: \"nil_endorsement_api_database\", \"elapsedTime\": elapsedTime, \"xmlrequest\": client.lastRequest });\n                    if (err) {\n                        app.log(err, \"ERROR in nilEndorsement\");\n                        errorMessage(crmData, args.body, rawRequest, err, res, 'Open', elapsedTime);\n                        // return resolve();\n                    } else if (res.statusCode === 500) {\n                        app.sendTextMessage('500 error')\n                        errorMessage(crmData, args.body, rawRequest, err, res, 'Open', elapsedTime);\n                        // return resolve();\n                    } else {\n                        try {\n                            if (typeof res === 'string') {\n                                res = JSON.parse(res);\n                            }\n                            if (res.WebService_NilEndorsementResult && res.WebService_NilEndorsementResult.ErrorLog && res.WebService_NilEndorsementResult.ErrorLog.length > 0) {\n                                let failureMessage = res.WebService_NilEndorsementResult.ErrorLog[0];\n                                if (app.UAT_ENV && failureMessage.ProposalNo === \"\") {\n                                    app.sendTextMessage('ERROR \\n' + failureMessage.Message).then(() => {\n                                        successMessage(crmData, '', args.body, rawRequest, err, res, 'Closed', elapsedTime);\n                                        // return resolve();\n                                    });\n                                } else if (failureMessage.ProposalNo !== '') {\n                                    app.sendTextMessage('Your ENdorsement is done proposal number is ' + failureMessage.ProposalNo).then(() => {\n                                        successMessage(crmData, failureMessage.ProposalNo, args.body, rawRequest, err, res, 'Closed', elapsedTime);\n                                        // return resolve();\n                                    });\n                                } else {\n                                    app.sendTextMessage('Your ENdorsement is done').then(() => {\n                                        successMessage(crmData, failureMessage.Message, args.body, rawRequest, err, res, 'Closed', elapsedTime);\n                                        // return resolve();\n                                    });\n                                }\n                            } else {\n                                app.sendTextMessage('Your ENdorsement is done').then(() => {\n                                    successMessage(crmData, '', args.body, rawRequest, err, res, 'Closed', elapsedTime);\n                                    // return resolve();\n                                });\n                            }\n                        } catch (err) {\n                            app.log(err, \"CATCH EROR\");\n                            app.sendTextMessage('ERROR')\n                        };\n                    }\n\n                });\n            });\n        })\n    });\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-25T09:06:26.619Z",
          "email": "parvez@yellowmessenger.com",
          "name": "endorsementApi",
          "__v": 0
        },
        {
          "_id": "5c611fbc521f1e0011c7ac30",
          "code": "//test 0235031324\n\nconst getDate = () => {\n    let today = new Date();\n    let dd = today.getDate();\n    let mm = today.getMonth() + 1; //January is 0!\n    let yyyy = today.getFullYear();\n\n    if (dd < 10) {\n        dd = '0' + dd;\n    }\n    if (mm < 10) {\n        mm = '0' + mm;\n    }\n    today = dd + '/' + mm + '/' + yyyy;\n    return today;\n}\n\n//Change in Customer Details\n//Alteration Of Customer Information\n\nreturn new Promise(resolve => {\n    const steps = app.context.steps;\n    let typeOfEndorsement = \"Alteration of Customer information\"\n    let curDate = getDate();\n    let curTime = new Date();\n    curTime = new Date(curTime.getTime() + 330 * 60000).toLocaleTimeString().split(':');\n    curTime = curTime[0] + \":\" + curTime[1];\n\n    let source = 0;\n    let medium = 0;\n    let campaign = 0;\n\n    let crmData = {\n        username: steps['cust-name'],\n        mobileNo: steps['mobile-number'],\n        email: steps['email-id'],\n        policyNo: steps['policy-number'],\n        leadId: \"\",\n        claimNo: \"\",\n        callerRelation: \"\"\n    };\n\n    let reqBody = `<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:mot=\"http://stub.unotechsoft.com/wsdl/MotorEndorsementService/\" xmlns:web=\"WebService_NilEndorsement\">\n   <soapenv:Header/>\n   <soapenv:Body>\n      <mot:webServiceNilEndorsement>\n         <!--Optional:-->\n         <mot:source>${source}</mot:source>\n         <!--Optional:-->\n         <mot:medium>${medium}</mot:medium>\n         <!--Optional:-->\n         <mot:campaign>${campaign}</mot:campaign>\n         <!--Optional:-->\n         <mot:strServiceToken/>\n         <!--Optional:-->\n         <mot:UserId>TASKUSER</mot:UserId>\n         <!--Optional:-->\n         <mot:objNilEndorsement_Details>\n            <!--Optional:-->\n            <web:Product_Code>${steps.productCode}</web:Product_Code>\n            <!--Optional:-->\n            <web:Proposal_ID>${steps.proposalNumber}</web:Proposal_ID>\n            <!--Optional:-->\n            <web:Type_Of_Endorsement>${typeOfEndorsement}</web:Type_Of_Endorsement>\n            <!--Optional:-->\n            <web:Options_For_Mid_Term_Adjustment>Pro Rata</web:Options_For_Mid_Term_Adjustment>\n            <web:Endorsement_Date>${curDate}</web:Endorsement_Date>\n            <!--Optional:-->\n            <web:Endorsement_Effective_Date>${curDate}</web:Endorsement_Effective_Date>\n            <!--Optional:-->\n            <web:Endorsement_Effective_Time>${curTime}</web:Endorsement_Effective_Time>\n            <!--Optional:-->\n            <web:Reason_For_Endorsement>${steps.remark}</web:Reason_For_Endorsement>\n            <!--Optional:-->\n            <web:Inclusion_Of_Vehicle_Number>${steps['change-vehicle-number'] ? steps['change-vehicle-number'].toUpperCase() : \"\"}<web:Inclusion_Of_Vehicle_Number/>\n            <!--Optional:-->\n            <web:InsuredDetails>\n               <!--Optional:-->\n               <web:Insured/>\n               <!--Optional:-->\n               <web:RiskType/>\n               <!--Optional:-->\n               <web:Title/>\n               <!--Optional:-->\n               <web:Gender/>\n               <!--Optional:-->\n               <web:MaritalStatus/>\n            </web:InsuredDetails>\n            <!--Optional:-->\n            <web:CustomerDetails>\n               <!--Optional:-->\n               <web:Title>${steps['change-title'] ? steps['change-title'] : ''}</web:Title>\n               <!--Optional:-->\n               <web:Gender/>\n               <!--Optional:-->\n               <web:MaritalStatus>${steps['change-marital-status'] ? steps['change-marital-status'].toUpperCase() : \"\"}</web:MaritalStatus>\n               <!--Optional:-->\n               <web:Occupation>${steps['change-occupation'] ? steps['change-occupation'].toUpperCase() : \"\"}<web:Occupation/>\n               <!--Optional:-->\n               <web:AddressType/>\n               <!--Optional:-->\n               <web:AddressLine1/>\n               <!--Optional:-->\n               <web:AddressLine2/>\n               <!--Optional:-->\n               <web:AddressLine3/>\n               <!--Optional:-->\n               <web:Landmark/>\n               <!--Optional:-->\n               <web:Country/>\n               <!--Optional:-->\n               <web:State/>\n               <!--Optional:-->\n               <web:District/>\n               <!--Optional:-->\n               <web:City/>\n               <!--Optional:-->\n               <web:Pincode/>\n               <!--Optional:-->\n               <web:Aadhaar_Number>${steps['change-aadhaar-number'] ? steps['change-aadhaar-number'] : \"\"}<web:Aadhaar_Number/>\n               <!--Optional:-->\n               <web:PAN_Number>${steps['change-pan-card'] ? steps['change-pan-card'].toUpperCase() : \"\"}<web:PAN_Number/>\n               <!--Optional:-->\n               <web:PrimaryPhone/>\n               <!--Optional:-->\n               <web:AlternatePhone/>\n               <!--Optional:-->\n               <web:MobileNo/>\n               <!--Optional:-->\n               <web:AlternateMobileNo>${steps['change-contact-number'] ? steps['change-contact-number'] : \"\"}<web:AlternateMobileNo/>\n               <!--Optional:-->\n               <web:EmailID>${steps['change-email-id'] ? steps['change-email-id'] : \"\"}<web:EmailID/>\n               <!--Optional:-->\n               <web:AlternateEmailID>${steps['change-alternate-email-id'] ? steps['change-alternate-email-id'] : \"\"}<web:AlternateEmailID/>\n            </web:CustomerDetails>\n         </mot:objNilEndorsement_Details>\n      </mot:webServiceNilEndorsement>\n   </soapenv:Body>\n</soapenv:Envelope>\n              `\n//Response for future reference\n    // app.sendTextMessage(app.renderMessage('nil-wait', {}, '')).then(() => {\n    //     const startTime = new Date();\n    //     app.request(options, function (err, res, body) {\n    //         app.elapsedTime(startTime).then((elapsedTime) => {\n    //             app.log(res, \"CLiend\");\n    //             app.log(err, \"ERROR in API\");\n    //             if (err || res.statusCode != 200) {\n    //                 app.sendTextMessage('eror')\n    //             } else {\n    //                 app.sendTextMessage('got response');\n    //                 app.sendTextMessage(body);\n    //                 // if (result.WebService_NilEndorsementResult && result.WebService_NilEndorsementResult.ErrorLog && result.WebService_NilEndorsementResult.ErrorLog[0].ProposalNo) {\n    //                 //     successMessage(crmData, result.WebService_NilEndorsementResult.ErrorLog[0].ProposalNo, body, result, err, elapsedTime, client);\n    //                 //     return resolve();\n    //                 // } else {\n    //                 //     if (result.WebService_NilEndorsementResult && result.WebService_NilEndorsementResult.ErrorLog && result.WebService_NilEndorsementResult.ErrorLog[0].Message && app.UAT_ENV) {\n    //                 //         app.sendTextMessage(\"ERROR : \" + result.WebService_NilEndorsementResult.ErrorLog[0].Message).then(() => {\n    //                 //             app.triggerIntent('anything-else', {});\n    //                 //             return;\n    //                 //         })\n    //                 //     }\n    //                 // }\n    //             }\n    //         })\n    //     })\n    // });\n\n    app.log(reqBody, \"Request body in nilEndorsementAction\");\n\n    app.executeFunction('endorsementApi', {body : reqBody, crmData : crmData}).then(()=>{\n        return resolve();\n    });\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-12T05:35:24.970Z",
          "email": "parvez@yellowmessenger.com",
          "name": "nilEndorsementAction",
          "__v": 0
        },
        {
          "_id": "5c62528ec26e0f0012a0173f",
          "code": "//test 0235031324\n\nconst getDate = () => {\n    let today = new Date();\n    let dd = today.getDate();\n    let mm = today.getMonth() + 1; //January is 0!\n    let yyyy = today.getFullYear();\n\n    if (dd < 10) {\n        dd = '0' + dd;\n    }\n    if (mm < 10) {\n        mm = '0' + mm;\n    }\n    today = dd + '/' + mm + '/' + yyyy;\n    return today;\n}\n\n//Change in Customer Details\n//Alteration Of Customer Information\n\nreturn new Promise(resolve => {\n    const steps = app.context.steps;\n    let typeOfEndorsement = \"Alteration of Customer information\"\n    let curDate = getDate();\n    let curTime = new Date();\n    curTime = new Date(curTime.getTime() + 330 * 60000).toLocaleTimeString().split(':');\n    curTime = curTime[0] + \":\" + curTime[1];\n\n    let source = 0;\n    let medium = 0;\n    let campaign = 0;\n\n    let pincode = \"\";\n    let landmark = \"\";\n    let city = \"\";\n\n    if(steps.address === 'true'){\n        pincode = steps['change-pincode'];\n        landmark = steps['change-address'];\n        city = steps.cityname;\n    }\n\n    let crmData = {\n        username: steps['cust-name'],\n        mobileNo: steps['mobile-number'],\n        email: steps['email-id'],\n        policyNo: steps['policy-number'],\n        leadId: \"\",\n        claimNo: \"\",\n        callerRelation: \"\"\n    };\n    let reqBody =  {\n          \"source\": source,\n          \"medium\": medium,\n          \"campaign\": campaign,\n          \"strServiceToken\": \"\",\n          \"UserId\": \"TASKUSER\",\n          \"objNilEndorsement_Details\": {\n            \"Product_Code\": steps.productCode,\n            \"Proposal_ID\": steps.proposalNumber,\n            \"Type_Of_Endorsement\": typeOfEndorsement,\n            \"Options_For_Mid_Term_Adjustment\": \"Pro Rata\",\n            \"Endorsement_Date\": curDate,\n            \"Endorsement_Effective_Date\": curDate,\n            \"Endorsement_Effective_Time\": curTime,\n            \"Reason_For_Endorsement\": \"OK\",\n            \"Inclusion_Of_Vehicle_Number\": steps['change-vehicle-number'] ? steps['change-vehicle-number'].toUpperCase() : \"\",\n            \"InsuredDetails\": {\n              \"Insured\": \"\",\n              \"RiskType\": \"\",\n              \"Title\": \"\",\n              \"Gender\": \"\",\n              \"MaritalStatus\": \"\",\n              \"targetNSAlias\": \"tns\",\n              \"targetNamespace\": \"WebService_NilEndorsement\"\n            },\n            \"CustomerDetails\": {\n              \"Title\": steps['change-title'] ? steps['change-title'] : '',\n              \"Gender\": \"\",\n              \"MaritalStatus\": steps['change-marital-status'] ? steps['change-marital-status'].toUpperCase() : \"\",\n              \"Occupation\": steps['change-occupation'] ? steps['change-occupation'].toUpperCase() : \"\",\n              \"AddressType\": \"\",\n              \"AddressLine1\": city ? city : \"\",\n              \"AddressLine2\": \"\",\n              \"AddressLine3\": \"\",\n              \"Landmark\": landmark ? landmark : \"\",\n              \"Country\": \"\",\n              \"State\": \"\",\n              \"District\": \"\",\n              \"City\": \"\",\n              \"Pincode\": pincode ? pincode : \"\",\n              \"Aadhaar_Number\": steps['change-aadhaar-number'] ? steps['change-aadhaar-number'] : \"\",\n              \"PAN_Number\": steps['change-pan-card'] ? steps['change-pan-card'].toUpperCase() : \"\",\n              \"PrimaryPhone\": \"\",\n              \"AlternatePhone\": \"\",\n              \"MobileNo\": \"\",\n              \"AlternateMobileNo\": steps['change-contact-number'] ? steps['change-contact-number'] : \"\",\n              \"EmailID\": steps['change-email-id'] ? steps['change-email-id'] : \"\",\n              \"AlternateEmailID\": steps['change-alternate-email-id'] ? steps['change-alternate-email-id'] : \"\",\n              \"targetNSAlias\": \"tns\",\n              \"targetNamespace\": \"WebService_NilEndorsement\"\n            },\n            \"targetNSAlias\": \"ns1\",\n            \"targetNamespace\": \"WebService_NilEndorsement\"\n          },\n          \"targetNSAlias\": \"tns\",\n          \"targetNamespace\": \"http://stub.unotechsoft.com/wsdl/MotorEndorsementService/\"\n        };\n\n    app.log(reqBody, \"Request body in nilEndorsementAction\");\n\n    app.executeFunction('endorsementApi', {body : reqBody, crmData : crmData}).then(()=>{\n        return resolve();\n    });\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-25T09:31:47.412Z",
          "email": "parvez@yellowmessenger.com",
          "name": "nilJsonApi",
          "__v": 0
        },
        {
          "_id": "5c65058b5f49a80011483797",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const value = app.data.message;\n    if (value.startsWith('$-')) {\n        let pincode = value.replace('$-', '').split('--');\n        app.setStep('change-pincode', pincode[0]).then(() => {\n            app.log(value, \"dks salkd\")\n            app.setStep('cityname', pincode[1]);\n            app.pushData({ pincode: pincode[0] }, app.context.intent);\n            return resolve();\n        });\n    } else {\n        return resolve({\n            success:false,\n            question:'Please choose the pincode from the suggested list'\n        });\n        // app.executeFunction('searchQuery', {table : 'nil_pincode', es_query : {query:{match:{ pincode : result}}}}).then((result) => {\n        //     if (!result) {\n        //         app.sendTextMessage('pincode not found').then(()=>{\n        //             app.triggerIntent('anything-else', {});\n        //             return resolve();\n        //         });\n        //     } else {\n        //         app.setStep('change_pincode', result.pincode).then(() => {\n        //             app.pushData({ pincode: result.pincode }, app.context.intent);\n        //             return resolve();\n        //         });\n        //     }\n        // });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-25T09:43:14.602Z",
          "email": "parvez@yellowmessenger.com",
          "name": "nilPincodeValidator",
          "__v": 0
        },
        {
          "_id": "5c650979bd527300120c251d",
          "code": "return new Promise(function (resolve) {\n    if (app.term) {\n        app.dataStore.search({\n            table: \"nil_pincode\",\n            body: {\n                \"query\": {\n                    \"regexp\": { \"pincode\": app.term.toLowerCase() + \".*\" }\n                }\n            }\n        }).then((result) => {\n            resolve(app._.map(result.hits.hits, function (hit) {\n                app.log(hit, \"hit\")\n                return [hit._source.pincode, \"$-\" + hit._source.pincode + \"--\" + hit._source.address];\n            }));\n        }).catch(err=>{\n            app.log(err, \"ERROR\")\n            resolve([]);\n        });\n    } else { resolve([]); }\n})",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-25T09:42:57.657Z",
          "email": "parvez@yellowmessenger.com",
          "name": "pincodeAutoComplete",
          "__v": 0
        },
        {
          "_id": "5c65312bbb02fd0011719fb6",
          "code": "return new Promise(resolve => {\n    // Your logic goes here\n    const value = app.data.message;\n    if(value && value.length > 10){\n        app.pushData({change_address: value}, app.context.intent);\n        return resolve();\n    }else{\n        return resolve({\n            success:false,\n            question:'Please enter more 3 words for your new address.'\n        });\n    }\n});",
          "bot": "x1542952684229",
          "updatedTime": "2019-02-14T09:23:36.484Z",
          "email": "parvez@yellowmessenger.com",
          "name": "nilAddressValidator",
          "__v": 0
        }
      ]


stepIds = []
nilEndorsementSteps = []
validators = ['servicesValidator', 'nilPanValidator', 'nameValidator', 'nilEmailValidator', 'nilaadhaarValidator', 'nilAltEmailValidator', 'occupationValidator', 'nilPolicyValidator', 'nilPincodeValidator', 'nilAddressValidator']
nilFunctions = []

for step in steps:
    stepIds.append(step["id"])

for obj in stepObj:
    if obj["_id"] in stepIds:
        nilEndorsementSteps.append(obj)
        if "validators" in obj:
            for i in list(validator["func"] for validator in obj["validators"]):
                validators.append(i)



for func in functionsObj:
    if func["name"] in validators:
        nilFunctions.append(func)

print(len(validators))
print(nilEndorsementSteps)
print(nilFunctions)

