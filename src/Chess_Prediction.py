#체스데이터를 이용해 여러가지 데이터마이닝 누가 승리했는지 예측(분류)  #Won(white, late)#Loss(white, black)
import pandas as pd
import tensorflow as tf
import datetime

#데이터 불러오기
data = pd.read_csv('data/chess.csv', delimiter=',', header=None, skiprows=1, names=['turns','victory_status',
                                                                                    'winner','white_id','white_rating',
                                                                                    'black_id','black_rating','moves'])
#('vitory_state','white_rating','black_rating') 플레이에서 승리한 정보를 불러옴
stateList=['winner','victory_status','white_rating','black_rating']
winnerList=['white','black','draw'] #0,1,2 stateInfo,rateInfo
stateInfo={0:data,1:data,2:data,}
chessInfo=[pd.DataFrame,pd.DataFrame,pd.DataFrame]
df=pd.DataFrame

enumerate
#데이터 가공 stateList='resign' 'mate' 'draw' 'outoftime' nan
for i in range(3):
    stateInfo[i]=data[data['winner']==winnerList[i]][stateList]
    chessInfo[i] = pd.DataFrame(stateInfo[i])
    if i==2:
        df=pd.concat([chessInfo[i-2],chessInfo[i-1],chessInfo[i]])
        df['Difference']= df['white_rating'] - df['black_rating']

df.dropna(axis=1)

incode=pd.get_dummies(df)

#tensorboard
log_dir = "log" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard=tf.keras.callbacks.TensorBoard(log_dir=log_dir,histogram_freq=1)

#독립
independ=incode[['white_rating', 'black_rating', 'Difference',
                 'victory_status_draw', 'victory_status_mate',
                 'victory_status_outoftime','victory_status_resign']]
#종속
depend=incode[['winner_black', 'winner_draw', 'winner_white']]


#모델 구조
X=tf.keras.layers.Input(shape=[7])
Y=tf.keras.layers.Dense(3, activation='softmax')(X)
model=tf.keras.models.Model(X,Y)
model.compile(loss='categorical_crossentropy', metrics='accuracy')

#모델 학습
model.fit(independ, depend, epochs=200, callbacks=[tensorboard])