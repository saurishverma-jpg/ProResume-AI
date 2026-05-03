import streamlit as st

def apply_modern_styles():
    """Apply modern styles by loading the CSS file"""
    # Styles are now loaded from style.css in app.py
    pass

def page_header(title, subtitle=None):
    """Render a consistent page header"""
    st.markdown(
        f'''
        <div style="background:#111;border:1px solid #2a2a2a;border-bottom:3px solid #FF6B00;padding:1.5rem;border-radius:4px;margin-bottom:1.5rem;">
            <h1 style="color:#f0f0f0!important;-webkit-text-fill-color:#f0f0f0!important;margin:0;font-size:2rem;border:none;display:block;padding:0;">{title}</h1>
            {f'<p style="color:#999;margin:0.5rem 0 0 0;font-size:1rem;">{subtitle}</p>' if subtitle else ''}
        </div>
        ''',
        unsafe_allow_html=True
    )

def hero_section(title, subtitle=None, description=None):
    """Render a modern hero section"""
    if description and not subtitle:
        subtitle = description
        description = None
    
    st.markdown(
        f'''
        <div style="background:#111;border:1px solid #2a2a2a;border-bottom:3px solid #FF6B00;padding:2rem;border-radius:4px;margin-bottom:1.5rem;">
            <h1 style="color:#f0f0f0!important;-webkit-text-fill-color:#f0f0f0!important;margin:0;font-size:2.2rem;border:none;display:block;padding:0;">{title}</h1>
            {f'<div style="color:#FF6B00;font-size:1.1rem;margin-top:0.75rem;font-weight:500;">{subtitle}</div>' if subtitle else ''}
            {f'<p style="color:#999;margin-top:0.5rem;font-size:0.95rem;">{description}</p>' if description else ''}
        </div>
        ''',
        unsafe_allow_html=True
    )

def feature_card(icon, title, description):
    """Render a feature card"""
    st.markdown(f"""
        <div style="background:#111;border:1px solid #2a2a2a;border-radius:4px;padding:1.25rem;margin:0.5rem 0;transition:border-color 0.2s;" onmouseover="this.style.borderColor='#FF6B00'" onmouseout="this.style.borderColor='#2a2a2a'">
            <div style="color:#FF6B00;font-size:1.8rem;margin-bottom:0.75rem;">
                <i class="{icon}"></i>
            </div>
            <h3 style="color:#f0f0f0!important;-webkit-text-fill-color:#f0f0f0!important;margin:0 0 0.5rem 0;font-size:1.1rem;">{title}</h3>
            <p style="color:#999;margin:0;font-size:0.9rem;line-height:1.5;">{description}</p>
        </div>
    """, unsafe_allow_html=True)

def about_section(content, image_path=None, social_links=None):
    """Render a modern about section with profile image and social links"""
    st.markdown("""
        <div style="background:#111;border:1px solid #2a2a2a;border-radius:4px;padding:1.5rem;">
            <div class="profile-section">
    """, unsafe_allow_html=True)
    
    if image_path:
        st.image(image_path, use_column_width=False, width=200)
    
    uploaded_file = st.file_uploader("Upload profile picture", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        st.image(uploaded_file, use_column_width=False, width=200)
    
    if social_links:
        st.markdown('<div style="margin:1rem 0;display:flex;gap:1rem;">', unsafe_allow_html=True)
        for platform, url in social_links.items():
            st.markdown(f'<a href="{url}" target="_blank" style="color:#FF6B00;font-size:1.5rem;"><i class="fab fa-{platform.lower()}"></i></a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
            </div>
            <div style="color:#ccc;line-height:1.6;">{content}</div>
        </div>
    """, unsafe_allow_html=True)

def metric_card(label, value, delta=None, icon=None):
    """Render a metric card"""
    icon_html = f'<i class="{icon}" style="color:#FF6B00;margin-right:0.5rem;"></i>' if icon else ''
    delta_html = f'<div style="color:#FF6B00;font-size:0.85rem;margin-top:0.25rem;">{delta}</div>' if delta else ''
    
    st.markdown(f"""
        <div style="background:#111;border:1px solid #2a2a2a;border-left:3px solid #FF6B00;border-radius:4px;padding:1.25rem;margin:0.5rem 0;">
            <div style="display:flex;align-items:center;margin-bottom:0.5rem;">
                {icon_html}
                <div style="color:#999;font-size:0.85rem;text-transform:uppercase;letter-spacing:0.5px;">{label}</div>
            </div>
            <div style="color:#f0f0f0;font-size:1.8rem;font-weight:700;">{value}</div>
            {delta_html}
        </div>
    """, unsafe_allow_html=True)

def template_card(title, description, image_url=None):
    """Render a template card"""
    image_html = f'<img src="{image_url}" style="width:100%;border-radius:4px;margin-bottom:1rem;" />' if image_url else ''
    
    st.markdown(f"""
        <div style="background:#111;border:1px solid #2a2a2a;border-radius:4px;padding:1.25rem;transition:border-color 0.2s;" onmouseover="this.style.borderColor='#FF6B00'" onmouseout="this.style.borderColor='#2a2a2a'">
            {image_html}
            <h3 style="color:#f0f0f0!important;-webkit-text-fill-color:#f0f0f0!important;margin:0 0 0.5rem 0;">{title}</h3>
            <p style="color:#999;margin:0;font-size:0.9rem;">{description}</p>
        </div>
    """, unsafe_allow_html=True)

def feedback_card(name, feedback, rating):
    """Render a feedback card"""
    stars = "⭐" * int(rating)
    
    st.markdown(f"""
        <div style="background:#1a1a1a;border:1px solid #2a2a2a;border-radius:4px;padding:1.25rem;margin:0.5rem 0;transition:border-color 0.2s;" onmouseover="this.style.borderColor='#FF6B00'" onmouseout="this.style.borderColor='#2a2a2a'">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.75rem;">
                <div style="color:#f0f0f0;font-weight:600;">{name}</div>
                <div>{stars}</div>
            </div>
            <p style="color:#999;margin:0;font-size:0.9rem;line-height:1.5;">{feedback}</p>
        </div>
    """, unsafe_allow_html=True)

def loading_spinner(message="Loading..."):
    """Show a loading spinner"""
    st.markdown(f"""
        <div style="text-align:center;padding:2rem;">
            <div class="loading-spinner"></div>
            <p style="color:#999;margin-top:1rem;">{message}</p>
        </div>
    """, unsafe_allow_html=True)

def progress_bar(value, max_value, label=None):
    """Render a progress bar"""
    percentage = (value / max_value) * 100
    label_html = f'<div style="color:#999;font-size:0.85rem;margin-bottom:0.4rem;">{label}</div>' if label else ''
    
    st.markdown(f"""
        <div style="margin:0.75rem 0;">
            {label_html}
            <div style="background:#1a1a1a;border-radius:4px;overflow:hidden;height:8px;">
                <div style="background:#FF6B00;height:100%;width:{percentage}%;border-radius:4px;transition:width 0.3s;"></div>
            </div>
            <div style="color:#FF6B00;font-size:0.85rem;margin-top:0.3rem;font-weight:500;">{percentage:.1f}%</div>
        </div>
    """, unsafe_allow_html=True)

def tooltip(content, tooltip_text):
    """Render content with a tooltip"""
    st.markdown(f"""
        <div class="tooltip" data-tooltip="{tooltip_text}">
            {content}
        </div>
    """, unsafe_allow_html=True)

def data_table(data, headers):
    """Render a data table"""
    header_row = "".join([f"<th style='background:#1a1a1a;color:#FF6B00;padding:0.75rem;text-align:left;border-bottom:2px solid #FF6B00;font-weight:600;'>{header}</th>" for header in headers])
    rows = ""
    for row in data:
        cells = "".join([f"<td style='padding:0.75rem;border-bottom:1px solid #2a2a2a;color:#ccc;'>{cell}</td>" for cell in row])
        rows += f"<tr style='transition:background 0.15s;' onmouseover=\"this.style.background='#1a1a1a'\" onmouseout=\"this.style.background='transparent'\">{cells}</tr>"
    
    st.markdown(f"""
        <div style="overflow-x:auto;border:1px solid #2a2a2a;border-radius:4px;">
            <table style="width:100%;border-collapse:collapse;">
                <thead><tr>{header_row}</tr></thead>
                <tbody>{rows}</tbody>
            </table>
        </div>
    """, unsafe_allow_html=True)

def grid_layout(*elements):
    """Create a responsive grid layout"""
    st.markdown("""
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1rem;">
            {}
        </div>
    """.format("".join(elements)), unsafe_allow_html=True)

def alert(message, type="info"):
    """Display a modern alert message"""
    alert_colors = {
        "info": ("#FF6B00", "rgba(255,107,0,0.1)"),
        "success": ("#22c55e", "rgba(34,197,94,0.1)"),
        "warning": ("#FF6B00", "rgba(255,107,0,0.1)"),
        "error": ("#ef4444", "rgba(239,68,68,0.1)")
    }
    alert_icons = {
        "info": "ℹ️",
        "success": "✅",
        "warning": "⚠️",
        "error": "❌"
    }
    icon = alert_icons.get(type, "ℹ️")
    color, bg = alert_colors.get(type, alert_colors["info"])
    
    st.markdown(f"""
        <div style="background:{bg};border:1px solid {color};border-radius:4px;padding:1rem;margin:0.5rem 0;display:flex;align-items:center;gap:0.75rem;">
            <span style="font-size:1.2rem;">{icon}</span>
            <span style="color:#ccc;font-size:0.9rem;">{message}</span>
        </div>
    """, unsafe_allow_html=True)

def about_section(title, description, team_members=None):
    st.markdown(f"""
        <div style="background:#111;border:1px solid #2a2a2a;border-radius:4px;padding:2rem;margin:1.5rem 0;">
            <h2 style="color:#FF6B00!important;-webkit-text-fill-color:#FF6B00!important;margin-bottom:1rem;font-size:1.6rem;">{title}</h2>
            <p style="color:#999;line-height:1.6;font-size:1rem;max-width:800px;margin-bottom:1.5rem;">{description}</p>
            {generate_team_section(team_members) if team_members else ''}
        </div>
    """, unsafe_allow_html=True)

def generate_team_section(team_members):
    if not team_members:
        return ""
    
    team_html = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;margin-top:1.5rem;">'
    for member in team_members:
        team_html += f"""
            <div style="background:#1a1a1a;border:1px solid #2a2a2a;border-radius:4px;padding:1.25rem;text-align:center;transition:border-color 0.2s;" onmouseover="this.style.borderColor='#FF6B00'" onmouseout="this.style.borderColor='#2a2a2a'">
                <img src="{member['image']}" alt="{member['name']}" style="width:100px;height:100px;border-radius:4px;margin-bottom:0.75rem;object-fit:cover;">
                <h3 style="color:#f0f0f0!important;-webkit-text-fill-color:#f0f0f0!important;margin:0 0 0.25rem 0;font-size:1rem;">{member['name']}</h3>
                <p style="color:#FF6B00;margin:0;font-size:0.85rem;">{member['role']}</p>
            </div>
        """
    team_html += '</div>'
    return team_html

def render_feedback(feedback_data):
    """Render feedback with modern styling"""
    if not feedback_data:
        return
    
    feedback_html = """
    <div style="margin:1rem 0;">
        <h3 style="color:#FF6B00!important;-webkit-text-fill-color:#FF6B00!important;margin-bottom:1rem;font-size:1.2rem;border-bottom:2px solid #FF6B00;padding-bottom:0.5rem;display:inline-block;">Resume Analysis Feedback</h3>
        <div>
    """
    
    for category, items in feedback_data.items():
        if items:
            for item in items:
                feedback_html += f"""
                <div style="background:#1a1a1a;border:1px solid #2a2a2a;border-left:3px solid #FF6B00;border-radius:4px;padding:1rem;margin:0.5rem 0;">
                    <div style="color:#FF6B00;font-size:0.8rem;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:0.25rem;font-weight:600;">{category}</div>
                    <div style="color:#ccc;font-size:0.9rem;">{item}</div>
                </div>
                """
    
    feedback_html += """
        </div>
    </div>
    """
    
    st.markdown(feedback_html, unsafe_allow_html=True)

def render_analytics_section(resume_uploaded=False, metrics=None):
    """Render the analytics section of the dashboard"""
    if not metrics:
        metrics = {
            'views': 0,
            'downloads': 0,
            'score': 'N/A'
        }
    
    card_data = [
        ('fas fa-eye', 'Resume Views', metrics['views']),
        ('fas fa-download', 'Downloads', metrics['downloads']),
        ('fas fa-chart-line', 'Profile Score', metrics['score']),
    ]
    
    for icon, label, value in card_data:
        st.markdown(f"""
            <div style="background:#111;border:1px solid #2a2a2a;border-radius:4px;padding:1.5rem;text-align:center;margin-bottom:0.75rem;">
                <div style="color:#FF6B00;font-size:2rem;margin-bottom:0.75rem;">
                    <i class='{icon}'></i>
                </div>
                <h2 style="color:#f0f0f0!important;-webkit-text-fill-color:#f0f0f0!important;font-size:1.1rem;margin-bottom:0.5rem;">{label}</h2>
                <p style="color:#FF6B00;font-size:2rem;font-weight:700;margin:0;">{value}</p>
            </div>
        """, unsafe_allow_html=True)

def render_activity_section(resume_uploaded=False):
    """Render the recent activity section"""
    st.markdown("""
        <div style="background:#111;border:1px solid #2a2a2a;border-radius:4px;padding:1.5rem;height:100%;">
            <h2 style="color:#f0f0f0!important;-webkit-text-fill-color:#f0f0f0!important;font-size:1.2rem;margin-bottom:1rem;">
                <i class='fas fa-history' style='color:#FF6B00;margin-right:0.5rem;'></i> Recent Activity
            </h2>
    """, unsafe_allow_html=True)
    
    if resume_uploaded:
        st.markdown("""
            <div style="color:#ccc;">
                <p style="margin:0.5rem 0;font-size:0.95rem;padding-left:0.5rem;border-left:2px solid #FF6B00;">Resume uploaded and analyzed</p>
                <p style="margin:0.5rem 0;font-size:0.95rem;padding-left:0.5rem;border-left:2px solid #FF6B00;">Generated optimization suggestions</p>
                <p style="margin:0.5rem 0;font-size:0.95rem;padding-left:0.5rem;border-left:2px solid #FF6B00;">Updated profile score</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="text-align:center;padding:1.5rem;color:#666;">
                <i class='fas fa-upload' style='font-size:2rem;color:#FF6B00;margin-bottom:0.75rem;display:block;'></i>
                <p style="margin:0;font-size:0.95rem;color:#999;">Upload your resume to see activity</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def render_suggestions_section(resume_uploaded=False):
    """Render the suggestions section"""
    st.markdown("""
        <div style="background:#111;border:1px solid #2a2a2a;border-radius:4px;padding:1.5rem;height:100%;">
            <h2 style="color:#f0f0f0!important;-webkit-text-fill-color:#f0f0f0!important;font-size:1.2rem;margin-bottom:1rem;">
                <i class='fas fa-lightbulb' style='color:#FF6B00;margin-right:0.5rem;'></i> Suggestions
            </h2>
    """, unsafe_allow_html=True)
    
    if resume_uploaded:
        st.markdown("""
            <div style="color:#ccc;">
                <p style="margin:0.5rem 0;font-size:0.95rem;padding-left:0.5rem;border-left:2px solid #FF6B00;">Add more quantifiable achievements</p>
                <p style="margin:0.5rem 0;font-size:0.95rem;padding-left:0.5rem;border-left:2px solid #FF6B00;">Include relevant keywords</p>
                <p style="margin:0.5rem 0;font-size:0.95rem;padding-left:0.5rem;border-left:2px solid #FF6B00;">Optimize formatting</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="text-align:center;padding:1.5rem;color:#666;">
                <i class='fas fa-file-alt' style='font-size:2rem;color:#FF6B00;margin-bottom:0.75rem;display:block;'></i>
                <p style="margin:0;font-size:0.95rem;color:#999;">Upload your resume to get suggestions</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)