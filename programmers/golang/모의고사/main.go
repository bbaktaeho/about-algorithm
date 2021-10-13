package main

import (
	"sort"
)

type User struct {
	Id    int
	Score int
}

func solution(answers []int) []int {
	user1 := []int{1, 2, 3, 4, 5}
	user2 := []int{2, 1, 2, 3, 2, 4, 2, 5}
	user3 := []int{3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
	users := []User{}
	result := []int{}

	for i := 1; i <= 3; i++ {
		users = append(users, User{Id: i})
	}

	for i, a := range answers {
		if a == user1[i%5] {
			users[0].Score += 1
		}
		if a == user2[i%8] {
			users[1].Score += 1
		}
		if a == user3[i%10] {
			users[2].Score += 1
		}
	}

	sort.Slice(users, func(i, j int) bool {
		return users[i].Score > users[j].Score
	})

	for _, user := range users {
		if user.Score == users[0].Score {
			result = append(result, user.Id)
		}
	}

	sort.Ints(result)
	return result
}

func main() {
	solution([]int{1, 2, 3, 4, 5})
}
