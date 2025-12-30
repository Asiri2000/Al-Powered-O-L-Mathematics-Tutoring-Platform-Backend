import React, { useState } from 'react';
import { motion } from 'framer-motion';

export default function LearningSlide({ stepData, onNext }) {
  const [selectedOption, setSelectedOption] = useState(null);
  const [status, setStatus] = useState('idle'); // 'idle' | 'correct' | 'wrong'

  const handleCheck = () => {
    // Find the selected option object
    const option = stepData.options.find(opt => opt.id === selectedOption);
    
    if (option?.is_correct) {
      setStatus('correct');
      // Optional: new Audio('/sounds/correct.mp3').play();
    } else {
      setStatus('wrong');
      // Optional: new Audio('/sounds/wrong.mp3').play();
    }
  };

  return (
    <div className="flex flex-col h-full max-w-md mx-auto p-4 gap-6">
      
      {/* --- TOP SECTION: THEORY CARD --- */}
      {/* Only show if theory_text exists */}
      {stepData.theory_text && (
        <motion.div 
          initial={{ y: -20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          className="bg-blue-50 border-l-4 border-blue-500 p-4 rounded-r-lg shadow-sm"
        >
          <h3 className="text-xs font-bold text-blue-600 uppercase tracking-wide mb-1">
            Quick Tip
          </h3>
          <p className="text-gray-700 text-sm leading-relaxed">
            {stepData.theory_text}
          </p>
          {stepData.theory_media_url && (
            <img 
              src={stepData.theory_media_url} 
              alt="Visual Aid" 
              className="mt-3 rounded-md w-full h-32 object-contain bg-white" 
            />
          )}
        </motion.div>
      )}

      {/* --- MIDDLE SECTION: QUESTION --- */}
      <div className="flex-1 flex flex-col justify-center">
        <h2 className="text-xl font-bold text-gray-800 mb-6">
          {stepData.question_text}
        </h2>

        <div className="grid gap-3">
          {stepData.options.map((option) => (
            <motion.button
              key={option.id}
              whileTap={{ scale: 0.98 }}
              onClick={() => status === 'idle' && setSelectedOption(option.id)}
              className={`p-4 rounded-xl border-2 text-left font-medium transition-all ${
                selectedOption === option.id
                  ? status === 'correct'
                    ? 'bg-green-100 border-green-500 text-green-800'
                    : status === 'wrong'
                      ? 'bg-red-100 border-red-500 text-red-800'
                      : 'bg-blue-50 border-blue-400 text-blue-800'
                  : 'bg-white border-gray-200 hover:bg-gray-50'
              }`}
            >
              {option.option_text}
            </motion.button>
          ))}
        </div>
      </div>

      {/* --- BOTTOM SECTION: ACTION BUTTON --- */}
      <div className="pt-4 border-t border-gray-100">
        {status === 'idle' ? (
          <button 
            onClick={handleCheck}
            disabled={!selectedOption}
            className="w-full py-3 rounded-xl bg-gray-900 text-white font-bold disabled:opacity-50 hover:bg-black transition-colors"
          >
            CHECK ANSWER
          </button>
        ) : (
          <motion.button 
            initial={{ scale: 0.9 }}
            animate={{ scale: 1 }}
            onClick={() => {
                // Reset state for next slide
                setStatus('idle');
                setSelectedOption(null);
                onNext(status === 'correct');
            }}
            className={`w-full py-3 rounded-xl text-white font-bold shadow-lg ${
              status === 'correct' ? 'bg-green-500 hover:bg-green-600' : 'bg-red-500 hover:bg-red-600'
            }`}
          >
            {status === 'correct' ? 'CONTINUE' : 'GOT IT'}
          </motion.button>
        )}
      </div>
    </div>
  );
}