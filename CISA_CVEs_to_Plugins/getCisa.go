package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	// Request data
	response, err := http.Get("https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json")
	// Check for Error
	if err != nil {
		fmt.Println("Error")

	} else {
		// Print status code
		fmt.Println(response.StatusCode)
		defer response.Body.Close()
		// Read data
		data, err := io.ReadAll(response.Body)
		if err != nil {
			fmt.Println("Error")
		}
		fmt.Println(string(data))
		os.WriteFile("known_exploited_vulnerabilities.json", data, 0777)

	}
}
