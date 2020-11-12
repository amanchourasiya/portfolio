# Portfolio - A personal blogging app

This is a personal blogging app build in Django and hosted on Heroku.
This app is currently deployed at https://www.amanchourasiya.com .

## Getting Started

For running this app in your local development environment you will need a linux machine as the production server(gunicorn) is not available on windows. 

### Prerequisites

To get all dependencies required fot this project run this command.

```
pip3 install -r requirements.txt
```

Since this app uses S3 for storing static images and blog data some environment variables need to be supplied. Complete list of environment variables cane be found inside env-variables file in this reposotiry.

AWS S3 bucket should be created with public access and ImageKit.io (Image CDN for image optimization) has been used in this app so ImageKit CDN should be preconfigured with AWS s3 bucket.

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With Technologies

* [BootStrap](https://getbootstrap.com/) -Responsive, mobile-first front-end web development framework. 
* [jQuery](https://jquery.com/) -  Fast, small, and feature-rich JavaScript library

* [Django](https://www.djangoproject.com/) - Python-based free and open-source web framework
* [AWS S3](https://aws.amazon.com/s3/) - Cloud storage service
* [Boto 3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Amazon Web Services (AWS) SDK for Python
* [PostgreSQL](https://www.postgresql.org/) - Advanced, enterprise-class, and open-source relational database system.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Aman Chourasiya** - *Project setup ,backend,and deployment* - [Aman Chourasiya](https://github.com/amanchourasiya)
* **Anuj Chourasiya** - *Front-end and backend* - [Anuj Chourasiya](https://github.com/anuj-chourasiya)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* EditorJS for blog Editor


