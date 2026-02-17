import matplotlib.pyplot as plt
import matplotlib.patches as patches
import textwrap, os, datetime

# PATH & DATA
save_folder = "." 
# Day 0=Mon, 1=Tue, 2=Wed, 3=Thu, 4=Fri, 5=Sat, 6=Sun
# Start: 14.75 = 2:45 PM, Duration: 1.25 = 1h 15m
schedule_data = [
    {'day': 0, 'start': 10.0, 'duration': 1.0, 'label': 'Client: WPH', 'type': 'Client'},
    {'day': 1, 'start': 8.75, 'duration': 3.25, 'label': 'Greek Exegesis', 'type': 'Fixed'},
    {'day': 1, 'start': 13.5, 'duration': 4.0, 'label': 'Guided Leadership', 'type': 'Fixed'},
    {'day': 2, 'start': 14.75, 'duration': 1.25, 'label': 'Client: Mortdale', 'type': 'Client'},
    {'day': 2, 'start': 16.0, 'duration': 1.0, 'label': 'Client: Mascot', 'type': 'Client'},
    {'day': 3, 'start': 9.75, 'duration': 3.25, 'label': 'Hebrew Exegesis', 'type': 'Fixed'},
    {'day': 4, 'start': 10.0, 'duration': 1.0, 'label': 'Client: WPH', 'type': 'Client'},
    {'day': 6, 'start': 9.0, 'duration': 7.0, 'label': 'CPC Church & Fellowship', 'type': 'Sabbath'}
]

colors = {'Fixed':'#EF5350','Travel':'#90A4AE','Client':'#42A5F5','DeepWork':'#66BB6A','Admin':'#AB47BC','Sabbath':'#FFA726','Personal':'#8D6E63'}

def render_all():
    # Use a fixed target date for filtering logic
    now = datetime.datetime.now()
    # iPhone logic: If after 8 PM, show tomorrow
    target_date = now + datetime.timedelta(days=1) if now.hour >= 20 else now
    target_day_idx = target_date.weekday()

    for mode in ['pc', 'ipad', 'iphone']:
        # Define dimensions and filenames
        if mode == 'pc': 
            fig, ax = plt.subplots(figsize=(16,9))
            fname, dpi = 'pc_wallpaper.png', 100
        elif mode == 'ipad': 
            fig, ax = plt.subplots(figsize=(12,9))
            fname, dpi = 'ipad_wallpaper.png', 100
        else: # iphone
            fig, ax = plt.subplots(figsize=(9,19.5))
            fname, dpi = 'iphone_daily.png', 300
        
        # Setup Axis
        ax.set_ylim(23,6)
        ax.set_facecolor('#1E1E1E' if mode != 'iphone' else '#000000')
        fig.patch.set_facecolor('#1E1E1E' if mode != 'iphone' else '#000000')
        
        # Time-Line (Y-Axis)
        hours = range(6, 24)
        ax.set_yticks(hours)
        ax.set_yticklabels([f"{h}" for h in hours], color='#AAAAAA', fontsize=11, fontweight='bold')
        ax.tick_params(axis='y', pad=8, length=0)
        ax.grid(axis='y', color='#333', ls='--', alpha=0.5)
        
        for s in ax.spines.values(): s.set_visible(False)

        if mode != 'iphone':
            days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
            ax.set_xlim(-0.5, 6.5)
            ax.xaxis.tick_top()
            ax.set_xticks(range(7))
            ax.set_xticklabels(days, color='white', fontweight='bold')
            # Highlight Today
            today_idx = now.weekday()
            ax.add_patch(patches.Rectangle((today_idx-0.5, 6), 1, 18, color='#333', alpha=0.3, zorder=0))
        else:
            ax.set_xlim(-0.5, 0.5)
            ax.set_xticks([])
            # Special margin for iPhone Clock
            plt.subplots_adjust(left=0.18, right=0.95, top=0.75, bottom=0.05)

        # Plot Events
        for e in schedule_data:
            if mode == 'iphone' and e['day'] != target_day_idx: 
                continue
            
            x = 0 if mode == 'iphone' else e['day']
            width = 0.85 if mode == 'iphone' else 0.9
            
            rect = patches.FancyBboxPatch((x-(width/2), e['start']), width, e['duration'], 
                                        boxstyle="round,pad=0.02", 
                                        facecolor=colors.get(e['type'], '#555'), zorder=2)
            ax.add_patch(rect)
            
            wrapped_text = textwrap.fill(e['label'], width=12 if mode == 'iphone' else 15)
            ax.text(x, e['start']+(e['duration']/2), wrapped_text, 
                    ha='center', va='center', color='white', weight='bold', 
                    size=10 if mode == 'iphone' else 9, zorder=3)
            
        plt.savefig(fname, dpi=dpi, bbox_inches='tight' if mode != 'iphone' else None)
        plt.close(fig)
        print(f"Generated {fname}")

if __name__ == "__main__":
    render_all()
