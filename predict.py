import requests
import json
import re

utterance = [
"beginning_gross_capital",
"beginning_net_capital",
"high_water_mark",
"gross_transfer_amount",
"adjusted_net_capital",
"subscription_date",
"redemption_date",
"crystalized_incentive",
"net_transfer_amount",
"side_pockets",
"high_water_transfer_amount",
"incentive_fee",
"adjusted_high_water_mark",
"adjusted_gross_capital",
"adjusted_incentive_fees",
"pnl_allocation",
"gross_pnl_allocation",
"redemption_penalty",
"us_tax_withheld",
"net_pnl_allocation",
"ending_gross_capital",
"ending_net_capital",
"adjusted_ending_gross_capital",
"adjusted_ending_net_capital",
"fund_performance_fees",
"fund_management_fees",
"ytd_gain_loss",
"less_contributions",
"ending_unfunded_comitment",
"commitment_amount",
"distribution_to_lp",
"net_net_end_cap",
"si_carried_interest",
"ytd_management_fees",
"ytd_management_fees_offset",
"ytd_distribution_to_lp_capital",
"contributed_capital"
]

headers = {
    "x-auth-token" : "f0f572207b9e1d0065959f44bebaf30c94b519d11f827bb328cf5e24a95b5d91"
}

mapping = {}

for name in utterance:
    text = name.replace('_',' ')
    response = requests.get("https://botplatform.io/proxy/ml/predict?text="+ text +"&bot=bot_1532580318855&context=undefined&language=en", headers = headers)
    response = json.loads(response.text)
    if response['intent'] in mapping :
        print('Appending ' + name)
        mapping[response['intent']].append(name)
    else:
        print('Creating Array ' + name)
        mapping[response['intent']] = []
        mapping[response['intent']].append(name)

print(mapping)