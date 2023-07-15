# DP_sorting
使用方式: 直接用python執行，如: python3 DP_sorting.py

可修改參數:  
  min: 資料最小值，預設為0  
  max: 資料最大值，預設為1023  
  case_num: 資料個數，預設為3000  
  epsilon: DP強度，數值越小越安全，預設為0.05

輸出分數為每個DP後的值和原數值的差絕對值後的和  
會將原資料和兩種結果寫入DPoutput.csv


# DP_compare
使用方式: 直接用python執行，如: python3 DP_compare.py

比對了以下不同參數的結果:  
  max: 資料最大值，為1023或2047  
  epsilon: DP強度，數值越小越安全，為1, 0.1, 0.05, 0.02, 0.01

輸出分數為每個DP後的值和原數值的差絕對值後的和  
並計算其中可能因Overflow所產生的較大變化總值，其定義為若差>資料range/2則該筆資料發生Overflow  
會將各種執行結果的分數寫入DPcompare.csv
