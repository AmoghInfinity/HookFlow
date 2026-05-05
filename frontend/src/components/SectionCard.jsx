import CopyButton from './CopyButton'

const SECTION_META = {
  hooks:    { icon: '🎯', title: 'Hooks' },
  script:   { icon: '📝', title: 'Script' },
  caption:  { icon: '💬', title: 'Caption' },
  hashtags: { icon: '🏷️', title: 'Hashtags' },
  shotList: { icon: '🎬', title: 'Shot List' },
}

export default function SectionCard({ type, data, onRegenerate }) {
  const meta = SECTION_META[type]
  if (!meta) return null

  const getCopyText = () => {
    switch (type) {
      case 'hooks': return (data.hook_options || []).join('\n')
      case 'script': return data.script || ''
      case 'caption': return data.caption || ''
      case 'hashtags': return (data.hashtags || []).join(' ')
      case 'shotList': return (data.shot_list || []).join('\n')
      default: return ''
    }
  }

  return (
    <div className="section-card">
      <div className="section-header">
        <div className="section-title-group">
          <div className="section-icon">{meta.icon}</div>
          <h3 className="section-title">{meta.title}</h3>
        </div>
        <div className="section-actions">
          <CopyButton text={getCopyText()} />
          <button className="action-btn" onClick={onRegenerate} title="Regenerate">
            <span className="icon">↻</span>
            Regenerate
          </button>
        </div>
      </div>

      {type === 'hooks' && <HooksContent data={data} />}
      {type === 'script' && <ScriptContent data={data} />}
      {type === 'caption' && <CaptionContent data={data} />}
      {type === 'hashtags' && <HashtagsContent data={data} />}
      {type === 'shotList' && <ShotListContent data={data} />}
    </div>
  )
}

function HooksContent({ data }) {
  return (
    <div className="hooks-grid">
      {(data.hook_options || []).map((hook, i) => (
        <div key={i} className={`hook-card${hook === data.selected_hook ? ' selected' : ''}`}>
          {hook}
        </div>
      ))}
    </div>
  )
}

function ScriptContent({ data }) {
  return <pre className="script-block">{data.script || ''}</pre>
}

function CaptionContent({ data }) {
  return <p className="caption-block">{data.caption || ''}</p>
}

function HashtagsContent({ data }) {
  return (
    <div className="hashtags-wrap">
      {(data.hashtags || []).map((tag, i) => (
        <span key={i} className="hashtag-pill">{tag.startsWith('#') ? tag : `#${tag}`}</span>
      ))}
    </div>
  )
}

function ShotListContent({ data }) {
  return (
    <ol className="shot-list">
      {(data.shot_list || []).map((shot, i) => (
        <li key={i} className="shot-item">
          <span className="shot-num">{i + 1}</span>
          <span className="shot-text">{shot}</span>
        </li>
      ))}
    </ol>
  )
}
