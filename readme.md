# Readme

This is one of the Raymond Project initial research prototype versions by the Shinzen Young Foundation. You can learn more about Shinzen Young [here](https://unifiedmindfulness.com/team/shinzen-young-2/).

Virtual enviroment name: raymond-lite-env
Current packages used: \
conda   22.9.0 \
python  3.10.9 \
flask   2.2.3 \
flask-cors==3.0.10 \
dotenv_values==1.0.0 \
openai  0.26.4

Also, some node components were used:

- nodejs: 18.15.0
- create-react-app: 5.0.1

1) Install conda
2) Install nodejs
3) Activate conda
4) Type in terminal `conda create --name raymond-lite-env python=3.10.9 flask=2.2.2`
5) Type `conda activate raymond-lite-env`
6) Type `pip install openai==0.27.2 flask-cors==3.0.10 dotenv_values==1.0.0`

For the backend, type in terminal:

```
cd server
conda activate raymond-lite-env
python main.py
```

For the frontend:

```
cd client
npm run dev
```
