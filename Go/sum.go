package adgvkty

import (
	"fmt"
	"math"
)

// Sum ...
func Sum() {
	var sum float64
	var lim float64 = math.Pow(10, -5)

	for i := 1.0; ; i++ {

		value := 1 / math.Pow(i, 2)

		if value > lim {

			sum += value

		} else {

			fmt.Println(i, sum)
			break

		}
	}
}
