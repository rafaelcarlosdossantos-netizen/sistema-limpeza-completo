import { useState, useEffect } from 'react'

function App() {
  const [view, setView] = useState('home')
  const [status, setStatus] = useState('Conectando...')
  const [novoCliente, setNovoCliente] = useState({ cliente: '', data: '', valor: '' })
  const API_URL = 'https://sistema-limpeza-completo.vercel.app/api'

  const [servicos, setServicos] = useState([
    { id: 1, cliente: 'João Silva', data: '2024-03-20', status: 'Agendado', valor: 'R$ 150,00' },
    { id: 2, cliente: 'Maria Oliveira', data: '2024-03-21', status: 'Concluído', valor: 'R$ 200,00' }
  ] )

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setStatus(data.status))
      .catch(() => setStatus('Erro na conexão'))
  }, [])

  const handleSalvar = (e) => {
    e.preventDefault()
    const novo = {
      id: servicos.length + 1,
      ...novoCliente,
      status: 'Agendado'
    }
    setServicos([...servicos, novo])
    setNovoCliente({ cliente: '', data: '', valor: '' })
    setView('painel')
    alert('Agendamento salvo com sucesso!')
  }

  // TELA INICIAL
  if (view === 'home') {
    return (
      <div style={{ minHeight: '100vh', backgroundColor: '#f3f4f6', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '20px', fontFamily: 'sans-serif' }}>
        <div style={{ maxWidth: '400px', width: '100%', backgroundColor: 'white', borderRadius: '12px', boxShadow: '0 10px 25px rgba(0,0,0,0.1)', padding: '40px', textAlign: 'center' }}>
          <h1 style={{ fontSize: '24px', fontWeight: 'bold', color: '#2563eb', marginBottom: '20px' }}>Sistema de Gestão de Limpeza</h1>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            <button onClick={() => setView('painel')} style={{ width: '100%', padding: '12px', backgroundColor: '#2563eb', color: 'white', border: 'none', borderRadius: '6px', fontWeight: '600', cursor: 'pointer' }}>Acessar Painel</button>
          </div>
          <div style={{ marginTop: '25px', paddingTop: '20px', borderTop: '1px solid #e5e7eb' }}>
            <p style={{ fontSize: '12px', color: '#9ca3af' }}>Status do Servidor: <span style={{ color: '#10b981', fontWeight: 'bold' }}>{status}</span></p>
          </div>
        </div>
      </div>
    )
  }

  // TELA DE FORMULÁRIO
  if (view === 'novo') {
    return (
      <div style={{ minHeight: '100vh', backgroundColor: '#f3f4f6', padding: '40px', fontFamily: 'sans-serif' }}>
        <div style={{ maxWidth: '500px', margin: '0 auto', backgroundColor: 'white', padding: '30px', borderRadius: '12px', boxShadow: '0 4px 6px rgba(0,0,0,0.05)' }}>
          <h2 style={{ marginBottom: '20px', color: '#1e3a8a' }}>Novo Agendamento</h2>
          <form onSubmit={handleSalvar} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
            <input required placeholder="Nome do Cliente" value={novoCliente.cliente} onChange={e => setNovoCliente({...novoCliente, cliente: e.target.value})} style={{ padding: '10px', borderRadius: '6px', border: '1px solid #d1d5db' }} />
            <input required type="date" value={novoCliente.data} onChange={e => setNovoCliente({...novoCliente, data: e.target.value})} style={{ padding: '10px', borderRadius: '6px', border: '1px solid #d1d5db' }} />
            <input required placeholder="Valor (ex: R$ 150,00)" value={novoCliente.valor} onChange={e => setNovoCliente({...novoCliente, valor: e.target.value})} style={{ padding: '10px', borderRadius: '6px', border: '1px solid #d1d5db' }} />
            <div style={{ display: 'flex', gap: '10px', marginTop: '10px' }}>
              <button type="submit" style={{ flex: 1, padding: '12px', backgroundColor: '#10b981', color: 'white', border: 'none', borderRadius: '6px', fontWeight: '600', cursor: 'pointer' }}>Salvar</button>
              <button type="button" onClick={() => setView('painel')} style={{ flex: 1, padding: '12px', backgroundColor: '#6b7280', color: 'white', border: 'none', borderRadius: '6px', fontWeight: '600', cursor: 'pointer' }}>Cancelar</button>
            </div>
          </form>
        </div>
      </div>
    )
  }

  // TELA DO PAINEL
  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#f3f4f6', padding: '40px', fontFamily: 'sans-serif' }}>
      <div style={{ maxWidth: '900px', margin: '0 auto' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '30px' }}>
          <h1 style={{ fontSize: '28px', fontWeight: 'bold', color: '#1e3a8a' }}>Painel de Serviços</h1>
          <button onClick={() => setView('home')} style={{ padding: '8px 16px', backgroundColor: '#6b7280', color: 'white', border: 'none', borderRadius: '6px', cursor: 'pointer' }}>Sair</button>
        </div>
        <div style={{ backgroundColor: 'white', borderRadius: '12px', boxShadow: '0 4px 6px rgba(0,0,0,0.05)', padding: '20px' }}>
          <table style={{ width: '100%', borderCollapse: 'collapse' }}>
            <thead>
              <tr style={{ borderBottom: '2px solid #f3f4f6', textAlign: 'left' }}>
                <th style={{ padding: '12px', color: '#6b7280' }}>Cliente</th>
                <th style={{ padding: '12px', color: '#6b7280' }}>Data</th>
                <th style={{ padding: '12px', color: '#6b7280' }}>Status</th>
                <th style={{ padding: '12px', color: '#6b7280' }}>Valor</th>
              </tr>
            </thead>
            <tbody>
              {servicos.map(s => (
                <tr key={s.id} style={{ borderBottom: '1px solid #f3f4f6' }}>
                  <td style={{ padding: '12px', fontWeight: '500' }}>{s.cliente}</td>
                  <td style={{ padding: '12px' }}>{s.data}</td>
                  <td style={{ padding: '12px' }}><span style={{ padding: '4px 8px', borderRadius: '12px', fontSize: '12px', backgroundColor: s.status === 'Concluído' ? '#dcfce7' : '#fef9c3', color: s.status === 'Concluído' ? '#166534' : '#854d0e' }}>{s.status}</span></td>
                  <td style={{ padding: '12px' }}>{s.valor}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <button onClick={() => setView('novo')} style={{ marginTop: '20px', width: '100%', padding: '12px', backgroundColor: '#10b981', color: 'white', border: 'none', borderRadius: '6px', fontWeight: '600', cursor: 'pointer' }}>+ Novo Agendamento</button>
        </div>
      </div>
    </div>
  )
}

export default App
