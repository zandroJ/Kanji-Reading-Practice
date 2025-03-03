import React, { useState, useEffect } from 'react';
import Quiz from './components/Quiz';
import './App.css';

const App = () => {
  const [kanjiData, setKanjiData] = useState([]);
  const [originalKanjiData, setOriginalKanjiData] = useState([]);
  const [score, setScore] = useState(0);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    fetch('./kanji_data.json')
      .then((response) => response.json())
      .then((data) => {
        setKanjiData(data);
        setOriginalKanjiData(data); // No need for JSON parse/stringify here
      })
      .catch((err) => console.error('Error loading JSON:', err));
  }, []);

  // Updated to handle card removal
  const handleScoreUpdate = (isCorrect, kanji) => {
    if (isCorrect) {
      setKanjiData(prev => prev.filter(k => k.kanji !== kanji.kanji));
      setScore(prev => prev + 1);
    }
  };

  const updateProgress = () => {
    setProgress(prev => {
      const newProgress = prev + 100 / originalKanjiData.length;
      return Math.min(newProgress, 100);
    });
  };

  return (
    <div className="container">
      <h1>漢字の読み練習</h1>
      <div className="score-container">
        <span id="score">{score}</span>
      </div>
      <div className="progress-bar">
        <div className="progress" style={{ width: `${progress}%` }}></div>
      </div>
      <Quiz
        kanjiData={kanjiData}
        originalKanjiData={originalKanjiData}
        onScoreUpdate={handleScoreUpdate}  // Updated prop name
        onProgressUpdate={updateProgress}
      />
    </div>
  );
};

export default App;