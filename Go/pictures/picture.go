package picture

import (
	"fmt"
	"image"
	"log"

	"github.com/BurntSushi/graphics-go/graphics"
	"github.com/fogleman/gg"
	"github.com/nfnt/resize"
)

const (
	backgroundPATH string = "pictures/sea.jpg"
	picsPATH       string = "pictures/%v.png"
)

// RepresentationShip структура для передачи нужным нам
// на репрезентации данных про корабль
type RepresentationShip struct {
	Name          string  // имя файла нужного спрайта
	X, Y          int     // координаты на фоне
	Rotation      float64 // угол поворота (по часовой)
	Width, Height int     // нужные нам размеры спрайта в пикселях
}

func main() {
	var ships []RepresentationShip

	ships = []RepresentationShip{
		{
			Name:     "galley",
			X:        125,
			Y:        125,
			Rotation: 0.0,
			Width:    50,
			Height:   50,
		},
		{
			Name:     "barge",
			X:        725,
			Y:        825,
			Rotation: 45.0,
			Width:    50,
			Height:   50,
		},
	}
	DrawShips(&ships)
}

// DrawShips ...
func DrawShips(ships *[]RepresentationShip) {

	background, err := gg.LoadJPG(backgroundPATH)
	if err != nil {
		log.Println(err)
	}

	backgroundSize := background.Bounds().Size()

	dc := gg.NewContext(backgroundSize.X, backgroundSize.Y)

	dc.DrawImage(background, 0, 0)

	for _, ship := range *ships {

		dc.SetRGBA(0, 0, 0, 0.5)

		sprite, err := gg.LoadPNG(fmt.Sprintf(picsPATH, ship.Name))
		if err != nil {
			log.Println(err)
		}

		if sprite.Bounds().Max.X != ship.Width && sprite.Bounds().Max.Y != ship.Height {
			sprite = resize.Resize(uint(ship.Width), uint(ship.Height), sprite, resize.Lanczos3)
		}

		if ship.Rotation != 0.0 {

			rotatedSprite := image.NewRGBA(image.Rect(0, 0, ship.Height, ship.Width))

			graphics.Rotate(rotatedSprite, sprite, &graphics.RotateOptions{Angle: ship.Rotation})

			dc.DrawImage(rotatedSprite, ship.X, ship.Y)
			ship.X, ship.Y = ship.X+ship.Width/2, ship.Y+ship.Width/2
			dc.DrawCircle(float64(ship.X), float64(ship.Y), float64(ship.Width)*2)
			dc.Stroke()
		} else {
			dc.DrawImage(sprite, ship.X, ship.Y)
			ship.X, ship.Y = ship.X+ship.Width/2, ship.Y+ship.Width/2
			dc.DrawCircle(float64(ship.X), float64(ship.Y), float64(ship.Width)*2)
			dc.SetLineWidth(3)
			dc.Stroke()
		}

	}

	dc.SavePNG("out.png")
}
