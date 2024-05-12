import React, { useEffect, useState } from "react";
import axios from 'axios';
import "./page.css";


type Sentiment_type = 'good' | 'bad' | 'empty'

function Page() {
  const SERVER_URL: string = "http://127.0.0.1:5000/";
  const [inputValue, setInputValue] = useState<string>("");
  const [reivew, setReview] = useState<string>("Здесь будет ваш отзыв");
  const [sentiment, setSentiment] = useState<string>("Пусто");
  const [colorSent, setColorSent] = useState<Sentiment_type>("empty")

  async function get_sentiment(text: string = ""): Promise<Sentiment_type> {
    try {
      const resp = await axios.get<Sentiment_type>(SERVER_URL, {
        params: { text: text },
      });
      return resp.data;
    } catch (err) {
      console.log(`The request failed --> ${err}`);
      return "empty";
    }
  }

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    let res_to_sentiment = {
      'good': 'Положительнный',
      'bad': 'Негативный',
      'empty': 'Пусто'
    }
    const res: Sentiment_type = await (get_sentiment(inputValue));
    setReview(inputValue);
    setSentiment(res_to_sentiment[res])
    setColorSent(res)
    setInputValue("");
  }


  return (
    <div className="Page">
      <h1>Введите свой отзыв, чтобы оценить его настроение</h1>
      <form className="Page__form" onSubmit={handleSubmit}>
        <input className="Page__input" value={inputValue} 
        onChange={e => setInputValue(e.target.value)}></input>
        <button className="Page_button">Оценить</button>
      </form>
      <div className="previousReview">
        <p className="previousReview__left">{reivew}</p>
        <p className="previousReview__right" color-sent={colorSent}>{sentiment}</p>
      </div>
      <div className="desc">
        <p>Это учебный проект, позволяющий определить настроение отзыва к фильму.</p>
        <p>Для предсказания используется модель глубокого обучения с точностью 90%. Модель корректно работает с русским текстом, также рекомендуется использовать отзыв длиной от 5 слов.</p>
        <p>В качестве данных для обучения было выбрано 4000 отзывов с кинопоиска.</p>
        <p>Код для определения настроения написан на языке Python и использует библиотеки машинного и глубокого обучения [numpy, pandas, sklearn, spacy, tensorflow/keras, pickle, etc].</p>
        <p>На стороне клиента используется простое React приложение.</p>
      </div>
    </div>
  );
}

export default Page;
