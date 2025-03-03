import React from 'react';
import './Modal.css';
import { FaRedo } from 'react-icons/fa'; // Import the redo icon

const Modal = ({ score, total, onClose }) => {
  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <h2>Game Over!</h2>
        <p>Your score: {score}/{total}</p>
        
        {/* Add the Reset Button */}
        <button className="reset-button" onClick={onClose}>
          <FaRedo /> Play Again
        </button>
      </div>
    </div>
  );
};

export default Modal;