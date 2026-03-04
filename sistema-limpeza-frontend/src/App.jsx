import { useState, useEffect } from 'react'

function App() {
  const [status, setStatus] = useState('Conectando...')
  const API_URL = 'https://sistema-limpeza-completo.vercel.app/api'

  useEffect(( ) => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setStatus(data.status))
      .catch(() => setStatus('Erro na conexão'))
  }, [])

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#f3f4f6', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '20px', fontFamily: 'sans-serif' }}>
      <div style={{ maxWidth: '400px', width: '100%', backgroundColor: 'white', borderRadius: '12px', boxShadow: '0 10px 25px rgba(0,0,0,0.1)', padding: '40px', textAlign: 'center' }}>
        <h1 style={{ fontSize: '24px', fontWeight: 'bold', color: '#2563eb', marginBottom: '20px' }}>
          Sistema de Gestão de Limpeza
        </h1>
        
        <p style={{ color: '#4b5563', marginBottom: '30px' }}>
          Bem-vindo ao seu novo sistema de gestão.
        </p>
        
        <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
          <button onClick={() => alert('Acessando o Painel...')} style={{ width: '100%', padding: '12px', backgroundColor: '#2563eb', color: 'white', border: 'none', borderRadius: '6px', fontWeight: '600', cursor: 'pointer' }}>
            Acessar Painel
          </button>
          <button style={{ width: '100%', padding: '12px', backgroundColor: 'white', color: '#2563eb', border: '1px solid #2563eb', borderRadius: '6px', fontWeight: '600', cursor: 'pointer' }}>
            Configurações
          </button>
        </div>
        
        <div style={{ mt: '30px', paddingTop: '20px', borderTop: '1px solid #e5e7eb', marginTop: '25px' }}>
          <p style={{ fontSize: '12px', color: '#9ca3af' }}>
            Status do Servidor: <span style={{ color: status === 'Erro na conexão' ? '#ef4444' : '#10b981', fontWeight: 'bold' }}>{status}</span>
          </p>
        </div>
      </div>
    </div>
  )
}

export default App
