import { useState, useCallback } from 'react'

const DURATIONS = [15, 30, 60, 90]
const PLATFORMS = ['Instagram', 'YouTube Shorts']
const TONES = ['Energetic', 'Calm', 'Humorous', 'Inspirational', 'Bold', 'Conversational']
const STYLES = ['Default', 'Storytelling', 'Educational', 'Cinematic', 'Documentary', 'Vlog', 'Listicle', 'Funny', 'Dark']

export default function InputForm({ onSubmit, isLoading }) {
  const [topic, setTopic] = useState('')
  const [platform, setPlatform] = useState('Instagram')
  const [tone, setTone] = useState('Energetic')
  const [style, setStyle] = useState('Storytelling')
  const [duration, setDuration] = useState(30)

  const handleSubmit = useCallback((e) => {
    e.preventDefault()
    if (!topic.trim() || isLoading) return
    onSubmit({ topic: topic.trim(), platform, tone, style, duration })
  }, [topic, platform, tone, style, duration, isLoading, onSubmit])

  const handleKeyDown = useCallback((e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      handleSubmit(e)
    }
  }, [handleSubmit])

  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <div className="sidebar-logo">H</div>
        <h1>HookFlow</h1>
      </div>
      <p className="sidebar-tagline">AI-powered content engine for short-form video creators.</p>

      <form className="input-form" onSubmit={handleSubmit}>
        <div className="form-group">
          <label className="form-label" htmlFor="topic">Topic</label>
          <input
            id="topic"
            className="form-input"
            type="text"
            placeholder="e.g. Morning productivity routine"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            onKeyDown={handleKeyDown}
            autoFocus
          />
        </div>

        <div className="form-group">
          <label className="form-label" htmlFor="platform">Platform</label>
          <select id="platform" className="form-select" value={platform} onChange={(e) => setPlatform(e.target.value)}>
            {PLATFORMS.map(p => <option key={p} value={p}>{p}</option>)}
          </select>
        </div>

        <div className="form-group">
          <label className="form-label" htmlFor="tone">Tone</label>
          <select id="tone" className="form-select" value={tone} onChange={(e) => setTone(e.target.value)}>
            {TONES.map(t => <option key={t} value={t}>{t}</option>)}
          </select>
        </div>

        <div className="form-group">
          <label className="form-label" htmlFor="style">Style</label>
          <select id="style" className="form-select" value={style} onChange={(e) => setStyle(e.target.value)}>
            {STYLES.map(s => <option key={s} value={s}>{s}</option>)}
          </select>
        </div>

        <div className="form-group">
          <label className="form-label">Duration</label>
          <div className="duration-group">
            {DURATIONS.map(d => (
              <button
                key={d}
                type="button"
                className={`duration-btn${duration === d ? ' active' : ''}`}
                onClick={() => setDuration(d)}
              >
                {d}s
              </button>
            ))}
          </div>
        </div>

        <button type="submit" className="generate-btn" disabled={isLoading || !topic.trim()}>
          {isLoading ? (
            <>
              <span className="spinner" />
              Generating...
            </>
          ) : (
            <>✦ Generate Content</>
          )}
        </button>
      </form>
    </aside>
  )
}
