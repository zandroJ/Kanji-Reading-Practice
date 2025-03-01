import React, { useState, useEffect } from 'react';
import Quiz from './components/Quiz';
import './App.css';

const App = () => {
  const [kanjiData, setKanjiData] = useState([]);
  const [originalKanjiData, setOriginalKanjiData] = useState([]);
  const [score, setScore] = useState(0);
  const [progress, setProgress] = useState(0);

  // Fetch Kanji data
  useEffect(() => {
    fetch('./kanji_data.json')
      .then((response) => response.json())
      .then((data) => {
        setKanjiData(data);
        setOriginalKanjiData(JSON.parse(JSON.stringify(data)));
      })
      .catch((err) => console.error('Error loading JSON:', err));
  }, []);

  // Update score
  const updateScore = (correct) => {
    if (correct) {
      setScore(score + 1);
    }
  };

  // Update progress
  const updateProgress = () => {
    const newProgress = progress + 100 / originalKanjiData.length;
    setProgress(Math.min(newProgress, 100));
  };

  return (
    <div className="container">
      <h1>漢字の読み練習</h1>
      <div className="score-container">
        Score: <span id="score">{score}</span>
      </div>
      <div className="progress-bar">
        <div className="progress" style={{ width: `${progress}%` }}></div>
      </div>
      <Quiz
        kanjiData={kanjiData}
        originalKanjiData={originalKanjiData}
        onScoreUpdate={updateScore}
        onProgressUpdate={updateProgress}
      />
    </div>
  );
};

export default App;