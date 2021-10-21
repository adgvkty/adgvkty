package main

import "fmt"

const (
	intersectionX float64 = 35.0 / 76.0
	intersectionY float64 = -7.0 / 2.0
)

var triangleVertex map[string]map[string]float64 = map[string]map[string]float64{
	"B": {"X": intersectionX, "Y": 0},
	"C": {"X": 0, "Y": intersectionY},
}

func main() {
	var x, y float64

	fmt.Println("Введите x:")
	fmt.Scan(&x)
	fmt.Println("Введите y:")
	fmt.Scan(&y)

	m := (x*triangleVertex["B"]["Y"] - triangleVertex["B"]["X"]*y) / (triangleVertex["C"]["X"]*triangleVertex["B"]["Y"] - triangleVertex["B"]["X"]*triangleVertex["C"]["Y"])

	fmt.Println(m)
	if m >= 0 && m <= 1 {
		l := (x - m*triangleVertex["C"]["X"]) / triangleVertex["B"]["X"]
		if l >= 0 && (m+l) <= 1 {
			fmt.Println(true)
			return
		}
	}

	fmt.Println(false)
}
