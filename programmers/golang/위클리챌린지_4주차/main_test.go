package main

import "testing"

func Test_solution(t *testing.T) {
	type args struct {
		table      []string
		languages  []string
		preference []int
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{"t1", args{[]string{"SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"}, []string{"PYTHON", "C++", "SQL"}, []int{7, 5, 5}}, "HARDWARE"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := solution(tt.args.table, tt.args.languages, tt.args.preference); got != tt.want {
				t.Errorf("solution() = %v, want %v", got, tt.want)
			}
		})
	}
}
