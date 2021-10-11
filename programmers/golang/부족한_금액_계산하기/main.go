package main

func solution(price int, money int, count int) int64 {
	pay := (count * (2*price + (count-1)*price)) / 2
	if money < pay {
		return int64(pay) - int64(money)
	} else {
		return 0
	}
}
