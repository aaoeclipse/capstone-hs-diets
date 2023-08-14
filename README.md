# WellnessWizard

WellnessWizard is a powerful data science algorithm that leverages sophisticated instructions to provide the user with a healthy diet plan. Given a user's weight (in kilograms) and desired caloric intake (in calories), the program generates a weekly diet plan, from Monday to Sunday.

## Installation

1. Clone the repository:

```bash
$ git clone https://github.com/aaoeclipse/capstone-hs-diets
```
2. Ensure Python3 is installed in your environment:

```bash
$ python3 --version
```

If you do not have Python3 installed, follow this [guide](https://www.python.org/downloads/) for installation instructions.

3. Install `requirements.txt` file:
   
```bash
$ pip install -r requirements.txt
```
This project utilises various dependencies, including FastAPI, which is specified inside the `requirements.txt` file.

## Running the application

Run the application with the following command:

```bash
$ uvicorn main:app
```

## Usage

To use the API, send a POST request to the `/diet` endpoint. The required parameters are:

`kg`: User's weight in kilograms  
`calories`: User's desired daily caloric intake

Here is an example using python requests:

```python
url = "http://localhost:8000/diet"
data = {"kg": 70, "calories": 2000}
response = requests.post(url, data=data)
print(response.json())
```

In response to a successful request, the program generates a list of foods to eat from Monday to Sunday, tailored to the user's individual needs and goals.

## Contact

For any other questions, feel free to [open an issue](https://github.com/aaoeclipse/WellnessWizard/issues/new) or contact me directly through my [GitHub](https://github.com/aaoeclipse). 

Thank you for using WellnessWizard! 

Stay Healthy!