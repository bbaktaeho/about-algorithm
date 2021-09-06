#!/bin/sh

if [ $# -eq 0 ] || [ $# -gt 1 ]; then
    echo "만들려는 문제 이름을 입력해.."
    exit 1
fi

dir_name=$1
timestamp=`date +%Y%m%d%H%M`

if [ ! -d $dir_name ]; then
    mkdir $dir_name
else 
    echo "이미 존재하는 문제야"
    exit 1
fi

cd $dir_name
echo "package main" > main.go
echo "package main" > main_test.go
go mod init $timestamp