

def main():
    con = snowflake.connector.connect(
    user='rick',
    password='mejzyg-pafpov-9noXmi',
    account='TQNXPFG.BG28519',
    session_parameters={
        'QUERY_TAG': 'EndOfMonthFinancials',
    }
    )

    return con