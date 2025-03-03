import React, { useState, useEffect, useRef } from 'react';
import KanjiCard from './KanjiCard';
import Modal from './Modal'; // Import the Modal component


const Quiz = ({ kanjiData, originalKanjiData, onScoreUpdate, onProgressUpdate }) => {
  const [currentKanji, setCurrentKanji] = useState(null);
  const [userInput, setUserInput] = useState('');
  const [feedback, setFeedback] = useState('');
  const [isFeedbackVisible, setIsFeedbackVisible] = useState(false);
  const [showModal, setShowModal] = useState(false);
  const [finalScore, setFinalScore] = useState({ correct: 0, total: 0 });

  const correctSound = useRef(null);
  const wrongSound = useRef(null);
  const kanjiDataRef = useRef(kanjiData);

  // Sync ref with kanjiData updates
  useEffect(() => {
    kanjiDataRef.current = kanjiData;
  }, [kanjiData]);

  // Initialize the game
  useEffect(() => {
    if (kanjiDataRef.current.length > 0 && !currentKanji) {
      nextCard(kanjiDataRef.current);
    }
  }, [kanjiData]);

  // Improved shuffle function
  const shuffle = (array) => {
    const newArray = [...array];
    for (let i = newArray.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
    }
    return newArray;
  };

  // Reset game properly
  const resetGame = () => {
    kanjiDataRef.current = [...originalKanjiData]; // Reset the kanji data
    setCurrentKanji(null); // Clear the current kanji
    setUserInput(''); // Clear the input field
    setFeedback(''); // Clear feedback
    setIsFeedbackVisible(false); // Hide feedback
    setShowModal(false); // Hide modal if visible
    setFinalScore({ correct: 0, total: 0 }); // Reset score
    nextCard(kanjiDataRef.current); // Start a new game
  };

  // Get next card without repeats
  const getNextCard = (data) => {
    if (data.length === 0) {
      setFinalScore({
        correct: onScoreUpdate(),
        total: originalKanjiData.length
      });
      setShowModal(true);
      return null;
    }

    const shuffledData = shuffle(data);
    return shuffledData[0];
  };

  // Display Kanji with proper cleanup
  const displayKanji = (kanji) => {
    setCurrentKanji(kanji);
    setUserInput('');
    setFeedback('');
    setIsFeedbackVisible(false);
    setTimeout(() => document.getElementById('answerInput')?.focus(), 100);
  };

  const checkAnswer = () => {
    if (!currentKanji) return;

    const userInputLower = userInput.trim().toLowerCase();
    // Split by comma first, then trim each reading
    const correctReadings = currentKanji.reading.split(',').map(r => r.trim().toLowerCase());
    const correct = correctReadings.includes(userInputLower);

    setFeedback(correct ? `✅ Correct!<br>Meaning: ${currentKanji.meaning}` 
                      : `❌ Wrong! Correct: ${currentKanji.reading}<br>Meaning: ${currentKanji.meaning}`);
    setIsFeedbackVisible(true);

    // Disable input immediately
    document.getElementById('answerInput').disabled = true;

    // Play sound
    (correct ? correctSound : wrongSound).current.play();

    // Update parent components after a short delay
    setTimeout(() => {
      onScoreUpdate(correct, currentKanji);
      onProgressUpdate();
    }, 500); // Short delay before updating parent state

    // Move to next card after 1 second
    setTimeout(() => {
      nextCard(kanjiDataRef.current);
      setIsFeedbackVisible(false);
      document.getElementById('answerInput').disabled = false;
      document.getElementById('answerInput').focus();
    }, 1000);
  };

  // Move to next card
  const nextCard = (data) => {
    const nextKanji = getNextCard(data);
    if (nextKanji) displayKanji(nextKanji);
  };

  // Input handlers
  const handleInputChange = (e) => setUserInput(e.target.value);
  const handleKeyDown = (e) => e.key === 'Enter' && checkAnswer();

  // Modal functions
  const closeModal = () => {
    setShowModal(false);
    resetGame();
  };

  const handleReset = () => {
    if (window.confirm('Are you sure you want to reset the game?')) {
      resetGame();
    }
  };

  return (
     <div>
    <KanjiCard kanji={currentKanji} />
    
    {isFeedbackVisible && (
      <p className="feedback" dangerouslySetInnerHTML={{ __html: feedback }} />
    )}

    <div className="input-container">
      <input
        type="text"
        id="answerInput"
        placeholder="Type pronunciation"
        value={userInput}
        onChange={handleInputChange}
        onKeyDown={handleKeyDown}
        autoComplete="off"
        disabled={isFeedbackVisible}
      />
      <button 
        onClick={checkAnswer}
        disabled={isFeedbackVisible}
      >
        Submit
      </button>
    </div>

    <audio ref={correctSound} src="audio/correct.mp3" />
    <audio ref={wrongSound} src="audio/wrong.mp3" />

    {showModal && (
      <Modal
        score={finalScore.correct}
        total={finalScore.total}
        onClose={closeModal}
      />
    )}
  </div>
  );
};

export default Quiz;