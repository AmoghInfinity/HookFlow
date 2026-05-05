import { useState, useCallback } from 'react'

export default function CopyButton({ text }) {
  const [copied, setCopied] = useState(false)

  const handleCopy = useCallback(() => {
    navigator.clipboard.writeText(text).then(() => {
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    })
  }, [text])

  return (
    <button className={`action-btn${copied ? ' copied' : ''}`} onClick={handleCopy} title="Copy to clipboard">
      <span className="icon">{copied ? '✓' : '⎘'}</span>
      {copied ? 'Copied' : 'Copy'}
    </button>
  )
}
