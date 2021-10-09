package main

import "testing"

func Test_solution2(t *testing.T) {
	type args struct {
		x int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{name: "test1", args: args{10}, want: true},
		{name: "test1", args: args{12}, want: true},
		{name: "test1", args: args{11}, want: false},
		{name: "test1", args: args{13}, want: false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := solution2(tt.args.x); got != tt.want {
				t.Errorf("solution2() = %v, want %v", got, tt.want)
			}
		})
	}
}
