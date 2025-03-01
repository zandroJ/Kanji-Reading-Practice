import React, { useState, useEffect, useRef } from 'react';
import KanjiCard from './KanjiCard';

const Quiz = ({ kanjiData, originalKanjiData, onScoreUpdate, onProgressUpdate }) => {
  const [currentKanji, setCurrentKanji] = useState(null);
  const [userInput, setUserInput] = useState('');
  const [feedback, setFeedback] = useState('');
  const [isFeedbackVisible, setIsFeedbackVisible] = useState(false); // Add state to track feedback visibility

  const correctSound = useRef(null);
  const wrongSound = useRef(null);

  // Initialize the game
  useEffect(() => {
    if (kanjiData.length > 0) {
      nextCard(kanjiData);
    }
  }, [kanjiData]);

  // Shuffle Kanji data
  const shuffle = (array) => {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
  };
  function resetGame() {
    global.score = 0;
    global.progress = 0;
    document.getElementById('score').textContent = '0';
    document.getElementById('progress').style.width = '0%';

    // Restore the original Kanji data and shuffle again
    kanjiData.push(...global.originalKanjiData);
    shuffle(kanjiData);
  }

  // Get next card
  const getNextCard = (data) => {
    if (data.length === 0) {
      alert(`Game Over! Your score: ${onScoreUpdate()}/${originalKanjiData.length}`);
      resetGame();
      return null;
    }

    const kanji = data[Math.floor(Math.random() * data.length)];
    const updatedData = data.filter((k) => k !== kanji);
    shuffle(updatedData);
    return kanji;
  };

  // Display Kanji
  const displayKanji = (kanji) => {
    setCurrentKanji(kanji);
    setUserInput('');
    setFeedback('');
    setIsFeedbackVisible(false); // Reset feedback visibility when showing a new card
  };

  // Check answer
  const checkAnswer = () => {
    if (!currentKanji) return;

    const userInputLower = userInput.trim().toLowerCase();
    const correctReadings = currentKanji.reading.split(', ').map((r) => r.trim().toLowerCase());
    const correct = correctReadings.includes(userInputLower);

    const feedbackMessage = correct
      ? `✅ Correct!`
      : `❌ Wrong! Correct: ${currentKanji.reading}`;

    const meaningMessage = `Meaning: ${currentKanji.meaning}`;

    setFeedback(`${feedbackMessage}<br>${meaningMessage}`);
    setIsFeedbackVisible(true); // Set feedback as visible

    // Play sound
    if (correct) {
      correctSound.current.play();
    } else {
      wrongSound.current.play();
    }

    onScoreUpdate(correct);
    onProgressUpdate();

    // Move to next card after 2 seconds
    setTimeout(() => nextCard(kanjiData), 2000);
  };

  // Next card
  const nextCard = (data) => {
    const nextKanji = getNextCard(data);
    if (nextKanji) {
      displayKanji(nextKanji);
    }
  };

  // Handle input change
  const handleInputChange = (e) => {
    setUserInput(e.target.value);
  };

  // Handle key down
  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      checkAnswer();
    }
  };

  return (
    <div>
      <KanjiCard kanji={currentKanji} />
      <div className="input-container">
        <input
          type="text"
          id="answerInput"
          placeholder="Type pronunciation"
          value={userInput}
          onChange={handleInputChange}
          onKeyDown={handleKeyDown}
          autoComplete="off"
          disabled={isFeedbackVisible} // Disable input if feedback is visible
        />
        <button 
          id="submitButton" 
          onClick={checkAnswer}
          disabled={isFeedbackVisible} // Disable button if feedback is visible
        >
          Submit
        </button>
        <button id="nextButton" hidden>
          Next Card
        </button>
      </div>
      <p className="feedback" id="feedback" dangerouslySetInnerHTML={{ __html: feedback }}></p>

      {/* Audio elements */}
      <audio ref={correctSound} src="audio/correct.mp3"></audio>
      <audio ref={wrongSound} src="audio/wrong.mp3"></audio>
    </div>
  );
};

export default Quiz;
