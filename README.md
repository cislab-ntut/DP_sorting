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

# 測試結果  
下表為有預防overflow的情況，extra值為可能發生overflow的資料佔量  
| cases | sorted | unsort | sorted extra | unsort extra |
| --- | --- | --- | --- | --- |
| epsilon = 1 | 3107.0 | 7048.0 | 0 | 4088.0 |
| epsilon = 0.1 | 10035.0 | 61830.0 | 0 | 32049.0 |
| epsilon = 0.05 | 9022.0 | 119819.0 | 0 | 63505.0 |
| epsilon = 0.02 | 13153.0 | 283886.0 | 0 | 148312.0 |
| epsilon = 0.01 | 16169.0 | 492302.0 | 0 | 265764.0 |
| Double range, epsilon = 1 | 4133.0 | 7025.0 | 0 | 4092.0 |
| Double range, epsilon = 0.1 | 11197.0 | 53864.0 | 0 | 24254.0 |
| Double range, epsilon = 0.05 | 30467.0 | 130004.0 | 0 | 72152.0 |
| Double range, epsilon = 0.02 | 21414.0 | 294273.0 | 0 | 150860.0 |
| Double range, epsilon = 0.01 | 25447.0 | 528682.0 | 0 | 248456.0 |

下表則是不預防overflow，可發現和上表相比，epsilon影響量變化不大  
| cases | sorted | unsort |
| --- | --- | --- |
| epsilon = 1 | 1293.0 | 2844.0 |
| epsilon = 0.1 | 4687.0 | 30652.0 |
| epsilon = 0.05 | 7629.0 | 60857.0 |
| epsilon = 0.02 | 25858.0 | 150537.0 |
| epsilon = 0.01 | 74506.0 | 305039.0 |
| Double range, epsilon = 1 | 1740.0 | 2814.0 |
| Double range, epsilon = 0.1 | 6666.0 | 30123.0 |
| Double range, epsilon = 0.05 | 9345.0 | 60169.0 |
| Double range, epsilon = 0.02 | 20225.0 | 147640.0 |
| Double range, epsilon = 0.01 | 45375.0 | 282266.0 |

