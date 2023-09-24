import streamlit as st

def calculate_savings(avg_salary, avg_monthly_sales, num_employees):
    waste_ratio = 0.2237
    inefficient_expense = avg_salary * num_employees * waste_ratio

    hourly_wage = avg_salary / (9.88 * 21)
    expected_time_created_per_person = inefficient_expense / (hourly_wage * num_employees)
    total_expected_time_created = expected_time_created_per_person * num_employees

    expected_sales = avg_monthly_sales * total_expected_time_created / (9.88 * 21)

    return inefficient_expense, expected_sales, total_expected_time_created, expected_time_created_per_person, hourly_wage

st.title('HubSpot導入による非効率な経費と見込める売上計算シミュレーション')

with st.sidebar:
    st.header('入力項目')
    avg_salary = st.number_input('営業担当の平均月給', value=0, step=1, format='%d')
    avg_monthly_sales = st.number_input('1人月の平均売上額', value=0, step=1, format='%d')
    num_employees = st.number_input('雇用人数', value=0, step=1, format='%d')

    st.markdown('<style>div.stButton > button:first-child { background-color: red; color: white; }</style>', unsafe_allow_html=True)
    calculate_button = st.button('計算')

if calculate_button:
    inefficient_expense, expected_sales, total_expected_time_created, expected_time_created_per_person, hourly_wage = calculate_savings(avg_salary, avg_monthly_sales, num_employees)

    st.markdown(f"""
    ## :bar_chart: 計算結果 :bar_chart:
    ---
    ### :moneybag: **非効率な経費: {inefficient_expense:,.0f}円** :moneybag:
    ### :hourglass: **創出が期待できる時間（人数合計）: {total_expected_time_created:,.2f}時間** :hourglass:
    ### :hourglass_flowing_sand: **創出が期待できる時間（1人当たり）: {expected_time_created_per_person:,.2f}時間** :hourglass_flowing_sand:
    ### :chart_with_upwards_trend: **創出時間で見込める売上: {expected_sales:,.0f}円** :chart_with_upwards_trend:
    ---
    *注: これはあくまで推定値です。具体的な数値は、実際の状況によって異なる場合があります。*
    """)

    with st.expander("計算式のプロセス（クリックして展開）"):
        st.write(f"""
        ### 計算式の詳細
        - **非効率な経費（全体）:** {avg_salary}円 (平均月給) × {num_employees}人 (雇用人数) × 0.2237 (無駄な時間の比率) = {inefficient_expense:,.0f}円
        - **創出が期待できる時間（全体）:** {inefficient_expense:,.0f}円 / ({hourly_wage:,.2f}円 (時給) × {num_employees}人) × {num_employees}人 = {total_expected_time_created:,.2f}時間
        - **創出が期待できる時間（1人当たり）:** {inefficient_expense:,.0f}円 / {hourly_wage:,.2f}円 (時給) × {num_employees}人 = {expected_time_created_per_person:,.2f}時間
        - **創出時間で見込める売上:** {avg_monthly_sales:,.0f}円 (平均月間売上) × {total_expected_time_created:,.2f}時間 / (9.88 × 21) = {expected_sales:,.0f}円
        """)
