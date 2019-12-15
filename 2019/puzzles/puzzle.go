package puzzles

type PuzzleIface interface {
	GetTitle() (string, error)
	GetSlug() (string, error)
	Solve([]string) (ResultIface, error)
}

type ResultIface interface {
	Print()
}
