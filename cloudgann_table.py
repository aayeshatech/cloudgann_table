import math
import gradio as gr
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Zodiac signs with Unicode symbols
ZODIAC_SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", 
    "Leo", "Virgo", "Libra", "Scorpio", 
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# Global variable to store current data
current_data = []

def calc_degree(value):
    """Calculate degree from square root fractional part"""
    try:
        sqrt_val = math.sqrt(value)
        frac = sqrt_val - int(sqrt_val)
        deg = frac * 360
        return round(deg, 2)
    except:
        return 0

def degree_to_zodiac(degree):
    """Convert degree to zodiac sign with position"""
    try:
        deg = degree % 360
        sign_index = int(deg // 30)
        sign_degree = deg % 30
        sign = ZODIAC_SIGNS[sign_index]
        return f"{sign} {sign_degree:.2f}°"
    except:
        return "Invalid"

def classify_angle(degree, tolerance=5):
    """Classify angle type based on significant astronomical angles"""
    ordinal_angles = [45, 135, 225, 315]
    cardinal_angles = [90, 180, 270, 360]
    special_angles = [120, 275, 325]
    
    def close_to(target):
        diff = abs(degree - target)
        diff = min(diff, 360 - diff)
        return diff <= tolerance
    
    if any(close_to(a) for a in cardinal_angles):
        return 'Cardinal', '#a6f1a6'
    elif any(close_to(a) for a in ordinal_angles):
        return 'Ordinal', '#a6c8f1'
    elif any(close_to(a) for a in special_angles):
        return 'Special', '#f1d3a6'
    else:
        return 'Regular', '#ffffff'

def calculate_gann_data(base_value, factor, levels, tolerance):
    """Calculate GANN table data with advanced analytics"""
    global current_data
    
    try:
        sqrt_base = math.sqrt(base_value)
        data = []
        special_count = 0
        total_degrees = 0
        
        for level in range(1, levels + 1):
            up_val = round((sqrt_base + factor * level) ** 2)
            down_val = round((sqrt_base - factor * level) ** 2)
            up_deg = calc_degree(up_val)
            down_deg = calc_degree(down_val)
            up_zodiac = degree_to_zodiac(up_deg)
            down_zodiac = degree_to_zodiac(down_deg)
            
            up_type, up_color = classify_angle(up_deg, tolerance)
            down_type, down_color = classify_angle(down_deg, tolerance)
            
            if up_type != 'Regular':
                special_count += 1
            if down_type != 'Regular':
                special_count += 1
                
            total_degrees += up_deg + down_deg
            
            data.append({
                'Level': level,
                'Up_Value': up_val,
                'Up_Degree': up_deg,
                'Up_Zodiac': up_zodiac,
                'Up_Type': up_type,
                'Up_Color': up_color,
                'Down_Value': down_val,
                'Down_Degree': down_deg,
                'Down_Zodiac': down_zodiac,
                'Down_Type': down_type,
                'Down_Color': down_color
            })
        
        current_data = data
        return data, special_count, total_degrees / (levels * 2)
    except Exception as e:
        return [], 0, 0

def create_advanced_table(base_value, factor, levels, tolerance, show_chart):
    """Create simplified GANN table with better visibility"""
    try:
        data, special_count, avg_degree = calculate_gann_data(base_value, factor, levels, tolerance)
        
        if not data:
            return "Error in calculation", pd.DataFrame(), None
        
        print(f"Generated data for {len(data)} levels")  # Debug print
        
        # Create simplified HTML table
        html = f"""
        <div style="font-family: 'Arial', sans-serif; margin: 20px 0; max-width: 100%; overflow: visible;">
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        color: white; padding: 25px; border-radius: 15px 15px 0 0; text-align: center;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                <h2 style="margin: 0; font-size: 2rem; font-weight: 700;">
                    GANN Analysis Table - {levels} Levels ({len(data)} rows generated)
                </h2>
            </div>
            
            <div style="overflow-x: auto; overflow-y: visible; border-radius: 0 0 15px 15px; 
                        box-shadow: 0 4px 15px rgba(0,0,0,0.1); max-height: none;">
                <table style="width: 100%; border-collapse: collapse; background: white; min-width: 1200px;">
                    <thead style="background: linear-gradient(145deg, #2c3e50, #34495e);">
                        <tr>
                            <th style="padding: 20px 15px; border: 1px solid #ddd; font-weight: 700; color: white; 
                                       font-size: 1.2rem; text-align: center;">Sr.No</th>
                            <th style="padding: 20px 15px; border: 1px solid #ddd; font-weight: 700; color: white; 
                                       font-size: 1.2rem; text-align: center;">Up Level</th>
                            <th style="padding: 20px 15px; border: 1px solid #ddd; font-weight: 700; color: white; 
                                       font-size: 1.2rem; text-align: center;">Degree</th>
                            <th style="padding: 20px 15px; border: 1px solid #ddd; font-weight: 700; color: white; 
                                       font-size: 1.2rem; text-align: center;">Down Level</th>
                            <th style="padding: 20px 15px; border: 1px solid #ddd; font-weight: 700; color: white; 
                                       font-size: 1.2rem; text-align: center;">Degree</th>
                        </tr>
                    </thead>
                    <tbody>
        """
        
        # Generate all rows - ensure we iterate through ALL data
        for i, row in enumerate(data):
            row_bg = "#f8f9fa" if i % 2 == 0 else "#ffffff"
            
            html += f"""
                <tr style="background-color: {row_bg}; border-bottom: 1px solid #ddd;">
                    <td style="padding: 18px 15px; text-align: center; font-weight: 700; font-size: 1.2rem; 
                               color: #2c3e50; border: 1px solid #ddd;">
                        {row['Level']}
                    </td>
                    <td style="padding: 18px 15px; text-align: center; font-weight: 700; font-size: 1.3rem; 
                               color: #27ae60; border: 1px solid #ddd;">
                        {row['Up_Value']:,}
                    </td>
                    <td style="padding: 18px 15px; text-align: center; background-color: {row['Up_Color']}; 
                               font-weight: 600; border: 1px solid #ddd; color: #2c3e50;">
                        <div style="margin-bottom: 6px; font-size: 1.2rem; font-weight: 700;">{row['Up_Degree']}°</div>
                        <div style="font-size: 1rem; color: #34495e;">{row['Up_Zodiac']}</div>
                    </td>
                    <td style="padding: 18px 15px; text-align: center; font-weight: 700; font-size: 1.3rem; 
                               color: #e74c3c; border: 1px solid #ddd;">
                        {row['Down_Value']:,}
                    </td>
                    <td style="padding: 18px 15px; text-align: center; background-color: {row['Down_Color']}; 
                               font-weight: 600; border: 1px solid #ddd; color: #2c3e50;">
                        <div style="margin-bottom: 6px; font-size: 1.2rem; font-weight: 700;">{row['Down_Degree']}°</div>
                        <div style="font-size: 1rem; color: #34495e;">{row['Down_Zodiac']}</div>
                    </td>
                </tr>
            """
        
        html += """
                    </tbody>
                </table>
            </div>
        </div>
        """
        
        # Create DataFrame for display
        df_data = []
        for row in data:
            df_data.append([
                row['Level'],
                f"{row['Up_Value']:,}",
                f"{row['Up_Degree']}° ({row['Up_Type']})",
                row['Up_Zodiac'],
                f"{row['Down_Value']:,}",
                f"{row['Down_Degree']}° ({row['Down_Type']})",
                row['Down_Zodiac']
            ])
        
        df = pd.DataFrame(df_data, columns=[
            'Level', 'Up Value', 'Up Degree', 'Up Zodiac', 
            'Down Value', 'Down Degree', 'Down Zodiac'
        ])
        
        # Create chart if requested
        chart = None
        if show_chart:
            chart = create_degree_chart(data)
        
        return html, df, chart
        
    except Exception as e:
        error_html = f"""
        <div style="background: #ffe6e6; border: 2px solid #ff9999; 
                    border-radius: 10px; padding: 20px; text-align: center; color: #c62828; 
                    font-family: 'Arial', sans-serif;">
            <h3 style="margin: 0 0 10px 0; font-size: 1.3rem;">⚠️ Calculation Error</h3>
            <p style="margin: 10px 0; font-size: 1rem;">Error: {str(e)}</p>
        </div>
        """
        return error_html, pd.DataFrame(), None

def create_degree_chart(data):
    """Create interactive chart showing degree distribution"""
    try:
        levels = [row['Level'] for row in data]
        up_degrees = [row['Up_Degree'] for row in data]
        down_degrees = [row['Down_Degree'] for row in data]
        up_types = [row['Up_Type'] for row in data]
        down_types = [row['Down_Type'] for row in data]
        
        fig = go.Figure()
        
        # Add up degrees
        fig.add_trace(go.Scatter(
            x=levels,
            y=up_degrees,
            mode='markers+lines',
            name='Up Degrees',
            marker=dict(
                size=12,
                color=[{'Cardinal': '#4CAF50', 'Ordinal': '#2196F3', 'Special': '#FF9800', 'Regular': '#9E9E9E'}[t] for t in up_types],
                line=dict(width=3, color='white')
            ),
            line=dict(color='#667eea', width=4)
        ))
        
        # Add down degrees
        fig.add_trace(go.Scatter(
            x=levels,
            y=down_degrees,
            mode='markers+lines',
            name='Down Degrees',
            marker=dict(
                size=12,
                color=[{'Cardinal': '#4CAF50', 'Ordinal': '#2196F3', 'Special': '#FF9800', 'Regular': '#9E9E9E'}[t] for t in down_types],
                line=dict(width=3, color='white')
            ),
            line=dict(color='#764ba2', width=4)
        ))
        
        # Add horizontal lines for important angles
        for angle, name, color in [(90, '90°', '#4CAF50'), (180, '180°', '#4CAF50'), 
                                   (270, '270°', '#4CAF50'), (360, '360°', '#4CAF50'),
                                   (45, '45°', '#2196F3'), (135, '135°', '#2196F3'),
                                   (225, '225°', '#2196F3'), (315, '315°', '#2196F3')]:
            fig.add_hline(y=angle, line_dash="dash", line_color=color, opacity=0.6)
        
        fig.update_layout(
            title='GANN Degree Analysis Chart',
            xaxis_title='Level',
            yaxis_title='Degree (°)',
            template='plotly_white',
            height=600,
            showlegend=True,
            font=dict(size=14)
        )
        
        return fig
    except:
        return go.Figure()

def reset_form():
    """Reset form to default values"""
    return 3338, 0.11, 5, 5, False

# Enhanced custom CSS for modern dynamic styling
custom_css = """
.gradio-container {
    font-family: 'Arial', sans-serif !important;
}

.gr-button {
    background: linear-gradient(45deg, #667eea, #764ba2) !important;
    border: none !important;
    border-radius: 8px !important;
    color: white !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    padding: 10px 20px !important;
    transition: all 0.3s ease !important;
}

.gr-button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3) !important;
}

.gr-textbox, .gr-number {
    border-radius: 6px !important;
    border: 2px solid #ddd !important;
    transition: all 0.3s ease !important;
}

.gr-textbox:focus, .gr-number:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.1) !important;
}
"""

# Create Gradio interface
with gr.Blocks(css=custom_css, title="CloudGann Table", theme=gr.themes.Soft()) as demo:
    gr.HTML("""
    <div style="text-align: center; padding: 30px; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 15px; margin-bottom: 25px; color: white;">
        <h1 style="font-size: 2.8rem; margin: 0; font-weight: 800;">CloudGann Table</h1>
        <p style="font-size: 1.2rem; margin: 10px 0 0 0; opacity: 0.9;">
            Professional GANN Trading Calculator
        </p>
    </div>
    """)
    
    # Configuration Section - Row Layout
    gr.HTML("<h3 style='color: #2c3e50; font-size: 1.4rem; font-weight: 700; margin-bottom: 15px; text-align: center;'>⚙️ Configuration</h3>")
    
    with gr.Row():
        base_value = gr.Number(label="Base Value", value=3338, scale=1)
        factor = gr.Number(label="Factor", value=0.11, step=0.01, scale=1)
        levels = gr.Number(label="Levels", value=5, minimum=1, maximum=50, step=1, scale=1)
        tolerance = gr.Number(label="Tolerance (°)", value=5, minimum=1, maximum=15, step=1, scale=1)
        show_chart = gr.Checkbox(label="Show Chart", value=True, scale=1)
    
    with gr.Row():
        calculate_btn = gr.Button("🚀 Calculate", variant="primary", scale=1)
        reset_btn = gr.Button("🔄 Reset", variant="secondary", scale=1)
    
    # Results Section - Full Width
    gr.HTML("<h3 style='color: #2c3e50; font-size: 1.4rem; font-weight: 700; margin: 25px 0 15px 0; text-align: center;'>📊 Results</h3>")
    
    with gr.Tabs():
        with gr.TabItem("🎯 GANN Table"):
            table_output = gr.HTML()
        
        with gr.TabItem("📋 Data View"):
            dataframe_output = gr.Dataframe()
        
        with gr.TabItem("📈 Chart Analysis"):
            chart_output = gr.Plot()

    # Event handlers
    def update_interface(base_val, fact, lvls, tol, chart):
        return create_advanced_table(base_val, fact, lvls, tol, chart)

    calculate_btn.click(
        fn=update_interface,
        inputs=[base_value, factor, levels, tolerance, show_chart],
        outputs=[table_output, dataframe_output, chart_output]
    )
    
    reset_btn.click(
        fn=reset_form,
        outputs=[base_value, factor, levels, tolerance, show_chart]
    )

if __name__ == "__main__":
    demo.launch()
