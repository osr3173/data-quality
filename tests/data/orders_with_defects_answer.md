# orders_with_defects.csv 정답표

- 행 수: 11 (헤더 제외), 열 수: 4
- 결측: customer 2개 (order_id 1003, 1007), 나머지 컬럼 0개
- 중복 행: 1개 (order_id 1004 행이 한 번 더 들어감)
- 타입 불일치: amount 1개 (order_id 1005의 "abc")
- 이상값: amount 1개 (order_id 1008의 9,900,000)

참고: amount에 "abc"가 섞여 있어 pandas는 amount 컬럼을 문자열로 읽는다. 이때 "abc"는 결측으로 세어지지 않는다.
