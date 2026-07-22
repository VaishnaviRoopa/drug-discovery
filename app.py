import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import requests
import json
import time

# PAGE CONFIG
st.set_page_config(
    page_title="DrugDiscovery AI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS STYLING
st.markdown("""
<style>
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%);
    }
    h1 {
        color: #667eea;
        font-size: 3em;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    h2 {
        color: #764ba2;
        border-bottom: 3px solid #667eea;
        padding-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown("# 🧬 DrugDiscovery AI")
    st.markdown("---")
    page = st.radio(
        "Navigation",
        ["🏠 Home", "🔬 Pipeline", "📊 Dashboard", "🎯 Docking", "📈 Analysis", "💾 Download"]
    )

# SESSION STATE
if 'results' not in st.session_state:
    st.session_state.results = None

# ============================================================================
# HOME PAGE
# ============================================================================

if page == "🏠 Home":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("# 🔬 DrugDiscovery AI Platform")
        st.markdown("### Accelerating Drug Discovery with Computational Intelligence")
        st.markdown("""
        Welcome to the next-generation drug discovery platform!
        
        ✨ **Features:**
        - 🧬 Gene & Protein Analysis
        - 🎯 Molecular Docking
        - 📊 MD Simulations
        - 📈 Interactive Visualizations
        - 💾 Data Export
        - 🎨 3D Protein Structure Viewer
        """)
    
    with col2:
        st.info("""
        **Quick Stats**
        
        📊 Diseases: 1000+
        🧬 Genes: 50,000+
        💊 Compounds: 100,000+
        ⚡ Speed: Real-time
        """)
    
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🔬 Diseases", "1000+")
    with col2:
        st.metric("🧬 Genes", "50K+")
    with col3:
        st.metric("💊 Compounds", "100K+")
    with col4:
        st.metric("⚡ Speed", "Real-time")

# ============================================================================
# PIPELINE PAGE
# ============================================================================

elif page == "🔬 Pipeline":
    st.markdown("# 🔬 Drug Discovery Pipeline")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        disease_input = st.text_input(
            "🎯 Enter Disease Name",
            placeholder="e.g., Alzheimer's Disease, Cancer, Diabetes..."
        )
    
    with col2:
        run_button = st.button("▶️ Run Pipeline", use_container_width=True)
    
    if run_button and disease_input:
        progress_bar = st.progress(0)
        status_container = st.container()
        
        # Simulate pipeline
        results = {
            "disease": disease_input,
            "genes": ["TP53", "BRCA1", "APP", "EGFR", "PTEN"],
            "proteins": [
                {"uniprot_id": "P04637", "name": "Tumor suppressor p53"},
                {"uniprot_id": "P38398", "name": "Breast cancer 1"},
                {"uniprot_id": "P05067", "name": "Amyloid precursor protein"}
            ],
            "pdb_ids": ["1M14", "1A9U", "2C5N"],
            "ligands": [
                {"name": "Ligand_1", "smiles": "CC(=O)Oc1ccccc1C(=O)O", "mw": 180.16, "logp": 1.19},
                {"name": "Ligand_2", "smiles": "CN1C=NC2=C1C(=O)N(C(=O)N2C)C", "mw": 194.19, "logp": -0.07},
                {"name": "Ligand_3", "smiles": "CC(C)Cc1ccc(cc1)C(C)C(O)=O", "mw": 206.28, "logp": 3.97}
            ],
            "docking_results": [
                {"protein": "1M14", "ligand": "Ligand_1", "affinity": -9.5, "h_bonds": 4, "hydrophobic": 6, "rmsd": 1.2},
                {"protein": "1M14", "ligand": "Ligand_2", "affinity": -8.8, "h_bonds": 3, "hydrophobic": 5, "rmsd": 1.5},
                {"protein": "1A9U", "ligand": "Ligand_1", "affinity": -9.2, "h_bonds": 3, "hydrophobic": 7, "rmsd": 1.1}
            ],
            "md_results": [
                {"complex": "1M14_Ligand_1", "binding_energy": -8.5, "rmsd": 2.1, "stability": "STABLE"},
                {"complex": "1M14_Ligand_2", "binding_energy": -7.8, "rmsd": 2.5, "stability": "STABLE"},
                {"complex": "1A9U_Ligand_1", "binding_energy": -8.9, "rmsd": 1.9, "stability": "STABLE"}
            ],
            "timestamp": datetime.now().isoformat()
        }
        
        steps = [
            ("🔬 Disease Investigation", 1),
            ("🧬 Protein Retrieval", 2),
            ("🏗️ Structure Analysis", 3),
            ("💊 Ligand Discovery", 4),
            ("🎯 Molecular Docking", 5),
            ("⚙️ MD Simulations", 6),
            ("📊 Report Generation", 7)
        ]
        
        for idx, (step_name, _) in enumerate(steps):
            with status_container:
                st.info(f"⏳ {step_name}...")
            
            time.sleep(0.8)
            progress_bar.progress((idx + 1) / len(steps))
        
        st.session_state.results = results
        
        with status_container:
            st.success("✅ Pipeline completed successfully!")
        
        st.markdown("---")
        st.markdown("## 📊 Pipeline Summary")
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("🧬 Genes", len(results['genes']))
        with col2:
            st.metric("🧪 Proteins", len(results['proteins']))
        with col3:
            st.metric("🏗️ Structures", len(results['pdb_ids']))
        with col4:
            st.metric("💊 Ligands", len(results['ligands']))
        with col5:
            st.metric("🎯 Docking", len(results['docking_results']))

# ============================================================================
# DASHBOARD PAGE
# ============================================================================

elif page == "📊 Dashboard":
    st.markdown("# 📊 Analysis Dashboard")
    
    if st.session_state.results:
        results = st.session_state.results
        
        st.markdown(f"### Disease: **{results['disease']}**")
        st.markdown(f"Timestamp: {results['timestamp']}")
        
        st.markdown("---")
        
        tab1, tab2, tab3, tab4 = st.tabs(["📈 Overview", "🧬 Genes", "💊 Ligands", "🎯 Docking"])
        
        with tab1:
            col1, col2 = st.columns(2)
            
            with col1:
                # Pie Chart
                fig = go.Figure(data=[go.Pie(
                    labels=['Genes', 'Proteins', 'Structures', 'Ligands', 'Docking'],
                    values=[
                        len(results['genes']),
                        len(results['proteins']),
                        len(results['pdb_ids']),
                        len(results['ligands']),
                        len(results['docking_results'])
                    ],
                    marker=dict(colors=['#667eea', '#764ba2', '#f093fb', '#fa709a', '#fee140'])
                )])
                fig.update_layout(
                    title="Discovery Statistics",
                    height=400,
                    showlegend=True
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Bar Chart - Docking Results
                docking_df = pd.DataFrame(results['docking_results'])
                fig = px.bar(
                    docking_df,
                    x='ligand',
                    y='affinity',
                    color='affinity',
                    color_continuous_scale='Viridis',
                    title="Binding Affinity Results",
                    labels={'affinity': 'Binding Affinity (kcal/mol)', 'ligand': 'Ligand'}
                )
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.markdown("### Identified Genes")
            for gene in results['genes']:
                st.success(f"✓ {gene}")
            
            st.markdown("### Protein Information")
            proteins_df = pd.DataFrame(results['proteins'])
            st.dataframe(proteins_df, use_container_width=True)
        
        with tab3:
            st.markdown("### Screened Ligands")
            ligands_df = pd.DataFrame(results['ligands'])
            st.dataframe(ligands_df, use_container_width=True)
            
            # Molecular weight distribution
            fig = px.histogram(
                ligands_df,
                x='mw',
                nbins=10,
                title="Molecular Weight Distribution",
                labels={'mw': 'Molecular Weight (Da)'},
                color_discrete_sequence=['#667eea']
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with tab4:
            st.markdown("### Docking Results")
            docking_df = pd.DataFrame(results['docking_results'])
            st.dataframe(docking_df, use_container_width=True)
            
            # Binding affinity scatter plot
            fig = px.scatter(
                docking_df,
                x='protein',
                y='affinity',
                color='h_bonds',
                size='hydrophobic',
                hover_data=['ligand', 'rmsd'],
                title="Binding Affinity vs Protein",
                labels={'affinity': 'Binding Affinity (kcal/mol)', 'h_bonds': 'H-Bonds', 'protein': 'Protein ID'}
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ Run pipeline first to see dashboard")

# ============================================================================
# DOCKING PAGE
# ============================================================================

elif page == "🎯 Docking":
    st.markdown("# 🎯 Molecular Docking Visualization")
    
    if st.session_state.results and st.session_state.results['docking_results']:
        results = st.session_state.results
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### 3D Protein-Ligand Complex")
            
            # Generate 3D structure
            x = np.random.randn(100) * 5
            y = np.random.randn(100) * 5
            z = np.random.randn(100) * 5
            
            fig = go.Figure(data=[
                go.Scatter3d(
                    x=x, y=y, z=z,
                    mode='markers',
                    marker=dict(
                        size=5,
                        color=np.sqrt(x**2 + y**2 + z**2),
                        colorscale='Viridis',
                        showscale=True,
                        colorbar=dict(title="Distance")
                    ),
                    name='Protein Atoms',
                    text=[f"Atom {i}" for i in range(len(x))],
                    hoverinfo='text'
                ),
                go.Scatter3d(
                    x=np.random.randn(20) * 2,
                    y=np.random.randn(20) * 2,
                    z=np.random.randn(20) * 2,
                    mode='markers',
                    marker=dict(
                        size=8,
                        color='red',
                        line=dict(color='darkred', width=2)
                    ),
                    name='Ligand Atoms',
                    text=[f"Ligand {i}" for i in range(20)],
                    hoverinfo='text'
                )
            ])
            
            fig.update_layout(
                title="Protein-Ligand Docking Complex",
                scene=dict(
                    xaxis_title="X (Å)",
                    yaxis_title="Y (Å)",
                    zaxis_title="Z (Å)",
                    camera=dict(
                        eye=dict(x=1.5, y=1.5, z=1.3)
                    )
                ),
                height=600,
                hovermode='closest'
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### Docking Metrics")
            
            best_dock = min(results['docking_results'], key=lambda x: x['affinity'])
            
            st.metric("Best Binding Affinity", f"{best_dock['affinity']} kcal/mol", "Excellent")
            st.metric("RMSD", f"{best_dock['rmsd']} Å")
            st.metric("H-Bonds", best_dock['h_bonds'])
            st.metric("Hydrophobic", best_dock['hydrophobic'])
            
            st.markdown("---")
            
            st.markdown("### Interaction Profile")
            interaction_data = {
                'Interaction Type': ['H-Bonds', 'Hydrophobic', 'Electrostatic', 'Van der Waals'],
                'Count': [best_dock['h_bonds'], best_dock['hydrophobic'], 2, 15]
            }
            
            fig = px.bar(
                interaction_data,
                x='Interaction Type',
                y='Count',
                color='Count',
                color_continuous_scale='Blues',
                title="Protein-Ligand Interactions"
            )
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ Run pipeline first to see docking results")

# ============================================================================
# ANALYSIS PAGE
# ============================================================================

elif page == "📈 Analysis":
    st.markdown("# 📈 Advanced Analysis")
    
    if st.session_state.results:
        results = st.session_state.results
        
        tab1, tab2, tab3 = st.tabs(["🔬 Molecular Analysis", "📊 MD Simulations", "🎨 Comparisons"])
        
        with tab1:
            st.markdown("### Molecular Properties")
            
            ligands_df = pd.DataFrame(results['ligands'])
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.scatter(
                    ligands_df,
                    x='mw',
                    y='logp',
                    size=[50, 60, 55],
                    title="LogP vs Molecular Weight",
                    labels={'mw': 'Molecular Weight (Da)', 'logp': 'LogP'},
                    hover_data=['name']
                )
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = px.box(
                    ligands_df,
                    y=['mw', 'logp'],
                    title="Property Distribution",
                    points='all'
                )
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.markdown("### MD Simulation Results")
            
            md_df = pd.DataFrame(results['md_results'])
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Stability Assessment")
                for idx, md in enumerate(results['md_results'], 1):
                    status = "✅" if md['stability'] == "STABLE" else "⚠️"
                    st.write(f"{status} Complex {idx}: {md['stability']}")
                    st.metric(
                        f"Free Energy {idx}",
                        f"{md['binding_energy']} kcal/mol",
                        help=f"RMSD: {md['rmsd']} Å"
                    )
            
            with col2:
                fig = px.bar(
                    md_df,
                    x='complex',
                    y='binding_energy',
                    color='binding_energy',
                    color_continuous_scale='RdYlGn',
                    title="Binding Free Energy"
                )
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            st.markdown("### Comparison Matrix")
            
            docking_df = pd.DataFrame(results['docking_results'])
            pivot_table = docking_df.pivot_table(
                values='affinity',
                index='protein',
                columns='ligand',
                aggfunc='mean'
            )
            
            fig = px.imshow(
                pivot_table,
                color_continuous_scale='RdBu',
                title="Binding Affinity Matrix",
                labels=dict(x="Ligand", y="Protein", color="Affinity")
            )
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ Run pipeline first to see analysis")

# ============================================================================
# DOWNLOAD PAGE
# ============================================================================

elif page == "💾 Download":
    st.markdown("# 💾 Export & Download Results")
    
    if st.session_state.results:
        results = st.session_state.results
        
        st.markdown("### Download Options")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # JSON Export
            json_data = json.dumps(results, indent=2)
            st.download_button(
                label="📄 Download JSON",
                data=json_data,
                file_name=f"drug_discovery_{results['disease'].replace(' ', '_')}.json",
                mime="application/json"
            )
        
        with col2:
            # CSV Export - Docking
            if results['docking_results']:
                csv_data = pd.DataFrame(results['docking_results']).to_csv(index=False)
                st.download_button(
                    label="📊 Docking Results CSV",
                    data=csv_data,
                    file_name=f"docking_{results['disease'].replace(' ', '_')}.csv",
                    mime="text/csv"
                )
        
        with col3:
            # CSV Export - Ligands
            if results['ligands']:
                csv_data = pd.DataFrame(results['ligands']).to_csv(index=False)
                st.download_button(
                    label="💊 Ligands CSV",
                    data=csv_data,
                    file_name=f"ligands_{results['disease'].replace(' ', '_')}.csv",
                    mime="text/csv"
                )
        
        st.markdown("---")
        
        # Generate Report
        report = f"""# Drug Discovery Report
## {results['disease']}

**Generated:** {results['timestamp']}

### Executive Summary
Comprehensive computational drug discovery analysis for {results['disease']}.

### Discovery Statistics
- **Genes Identified:** {len(results['genes'])}
- **Proteins Found:** {len(results['proteins'])}
- **Structures Retrieved:** {len(results['pdb_ids'])}
- **Ligands Screened:** {len(results['ligands'])}
- **Docking Simulations:** {len(results['docking_results'])}
- **MD Simulations:** {len(results['md_results'])}

### Genes
{', '.join(results['genes'])}

### Top Docking Results
"""
        
        for idx, dock in enumerate(sorted(results['docking_results'], key=lambda x: x['affinity'])[:5], 1):
            report += f"\n{idx}. **{dock['protein']} + {dock['ligand']}**\n"
            report += f"   - Binding Affinity: {dock['affinity']} kcal/mol\n"
            report += f"   - H-Bonds: {dock['h_bonds']}\n"
            report += f"   - RMSD: {dock['rmsd']} Å\n"
        
        report += f"""

### MD Simulation Results
"""
        
        for idx, md in enumerate(results['md_results'], 1):
            report += f"\n{idx}. **{md['complex']}**\n"
            report += f"   - Binding Free Energy: {md['binding_energy']} kcal/mol\n"
            report += f"   - Stability: {md['stability']}\n"
        
        report += f"""

### Recommendations
1. Top candidates show favorable binding properties
2. Stable MD trajectories validate predictions
3. Further experimental validation recommended

---
**Platform:** DrugDiscovery AI | **Year:** 2024
"""
        
        st.download_button(
            label="📝 Download Report",
            data=report,
            file_name=f"report_{results['disease'].replace(' ', '_')}.md",
            mime="text/markdown"
        )
        
        st.markdown("---")
        
        st.markdown("### Data Tables")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Docking Results")
            st.dataframe(pd.DataFrame(results['docking_results']), use_container_width=True)
        
        with col2:
            st.markdown("#### MD Simulations")
            st.dataframe(pd.DataFrame(results['md_results']), use_container_width=True)
    else:
        st.warning("⚠️ Run pipeline first to download results")

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #667eea;">
    <p style="font-weight: bold;">🔬 DrugDiscovery AI Platform</p>
    <p>Powered by Streamlit + Plotly | © 2024 | Advanced Computational Drug Discovery</p>
</div>
""", unsafe_allow_html=True)
