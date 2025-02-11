# Full Body Detection FASTAPI using MMPose

## Pose Detection Results

These images are results.

<p align="center">
  <div style="display: inline-block; margin-right: 20px; text-align: center;">
    <img src="results/1.jpg" alt="First Image" width="400"/>
    <br />
    <strong>First Patient</strong>
  </div>
  <div style="display: inline-block; text-align: center;">
    <img src="results/1_result.jpg" alt="First Result Image" width="400"/>
    <br />
    <strong>Result of First Patient</strong>
  </div>
</p>

<p align="center">
  <div style="display: inline-block; margin-right: 20px; text-align: center;">
    <img src="results/2.jpg" alt="Second Image" width="400"/>
    <br />
    <strong>Second Patient</strong>
  </div>
  <div style="display: inline-block; text-align: center;">
    <img src="results/2_result.jpg" alt="Second Result Image" width="400"/>
    <br />
    <strong>Result of Second Patient</strong>
  </div>
</p>

<p align="center">
  <div style="display: inline-block; margin-right: 20px; text-align: center;">
    <img src="results/3.jpg" alt="Third Image" width="400"/>
    <br />
    <strong>Third Patient</strong>
  </div>
  <div style="display: inline-block; text-align: center;">
    <img src="results/3_result.jpg" alt="Third Result Image" width="400"/>
    <br />
    <strong>Result of Third Patient</strong>
  </div>
</p>

## Install Dependencies

1. Install miniconda from offical site.

2. Create a new environment

```
conda create --name openmmlab python=3.10
conda activate openmmlab
```

3. Install dependencies

```
pip install -r requirements.txt
```

## Run Backend API

Use this command to run server.

```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers {cpu_count}
```

In Linux, can get cpu count using this command.

```
lscpu
```

## Check API

This API can be checked in localhost.

Run server.

```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Here, '--reload' flag is optional.
With this flag, the api is updated automatically whenever the source code is changed.

REATAPI document can be found [here](http://localhost:8000/api/docs).

## PS

This is the reference [site](https://mmpose.readthedocs.io/en/latest/installation.html).
