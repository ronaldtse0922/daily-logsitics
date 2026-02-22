import matplotlib.pyplot as plt
import matplotlib.patches as patches
import textwrap
import os
import datetime

# 1. CLOUD PATH (Critical for GitHub)
save_folder = "." 

# 2. DATA 
schedule_data = [
    # MONDAY (Day 0)
    {'day': 0, 'start': 8.0, 'duration': 0.5, 'label': 'Wake & Bible', 'type': 'Personal'},
    {'day': 0, 'start': 9.5, 'duration': 0.5, 'label': 'Drive to WPH', 'type': 'Travel'},
    {'day': 0, 'start': 10.0, 'duration': 1.5, 'label': 'Client: WPH', 'type': 'Client'},
    {'day': 0, 'start': 11.5, 'duration': 0.5, 'label': 'Drive Home', 'type': 'Travel'},
    {'day': 0, 'start': 12.0, 'duration': 0.75, 'label': 'Transition Buffer', 'type': 'Personal'},
    {'day': 0, 'start': 12.75, 'duration': 2.0, 'label': 'Deep Work: Spaced Retrieval', 'type': 'DeepWork'},
    {'day': 0, 'start': 16.0, 'duration': 2.0, 'label': 'Admin: Billing', 'type': 'Admin'},
    {'day': 0, 'start': 18.0, 'duration': 1.0, 'label': 'Dinner', 'type': 'Personal'},
    {'day': 0, 'start': 19.5, 'duration': 2.0, 'label': 'Deep Work: Gen. Translation', 'type': 'DeepWork'},

    # TUESDAY (Day 1) - GATE A: INTENSIVE
    {'day': 1, 'start': 8.0, 'duration': 0.5, 'label': 'Wake & Bible', 'type': 'Personal'},
    {'day': 1, 'start': 8.5, 'duration': 0.25, 'label': 'Drive Burwood', 'type': 'Travel'},
    {'day': 1, 'start': 8.75, 'duration': 3.25, 'label': 'Class: Romans (Greek)', 'type': 'Fixed'},
    {'day': 1, 'start': 12.0, 'duration': 1.5, 'label': 'Lunch/Break', 'type': 'Personal'},
    {'day': 1, 'start': 13.5, 'duration': 4.0, 'label': 'Class: Guided Leadership', 'type': 'Fixed'},
    {'day': 1, 'start': 17.5, 'duration': 0.5, 'label': 'Drive Home', 'type': 'Travel'},
    {'day': 1, 'start': 18.0, 'duration': 0.75, 'label': 'Transition Buffer', 'type': 'Personal'},
    {'day': 1, 'start': 18.75, 'duration': 1.0, 'label': 'Dinner', 'type': 'Personal'},
    {'day': 1, 'start': 19.75, 'duration': 2.0, 'label': 'Deep Work: Mixed Parsing', 'type': 'DeepWork'},

    # WEDNESDAY (Day 2) - GATE A OVERFLOW & SABBATH 3
    {'day': 2, 'start': 8.0, 'duration': 0.5, 'label': 'Wake & Bible', 'type': 'Personal'},
    {'day': 2, 'start': 8.5, 'duration': 2.0, 'label': 'Deep Work: Syntax Diagram', 'type': 'DeepWork'},
    {'day': 2, 'start': 10.75, 'duration': 2.0, 'label': 'Deep Work: Argument Map', 'type': 'DeepWork'},
    {'day': 2, 'start': 12.75, 'duration': 1.0, 'label': 'Lunch', 'type': 'Personal'},
    {'day': 2, 'start': 13.75, 'duration': 1.0, 'label': 'Drive Mortdale', 'type': 'Travel'},
    {'day': 2, 'start': 14.75, 'duration': 0.75, 'label': 'Client: Mortdale', 'type': 'Client'},
    {'day': 2, 'start': 15.5, 'duration': 0.5, 'label': 'Drive Mascot', 'type': 'Travel'},
    {'day': 2, 'start': 16.0, 'duration': 1.0, 'label': 'Client: Mascot', 'type': 'Client'},
    {'day': 2, 'start': 17.0, 'duration': 0.75, 'label': 'Drive Home', 'type': 'Travel'},
    {'day': 2, 'start': 17.75, 'duration': 0.75, 'label': 'Transition Buffer', 'type': 'Personal'},
    {'day': 2, 'start': 18.5, 'duration': 0.5, 'label': 'Admin: Billing', 'type': 'Admin'},
    {'day': 2, 'start': 19.0, 'duration': 3.0, 'label': 'Sabbath Rest', 'type': 'Sabbath'},

    # THURSDAY (Day 3)
    {'day': 3, 'start': 8.0, 'duration': 0.5, 'label': 'Wake & Bible', 'type': 'Personal'},
    {'day': 3, 'start': 9.25, 'duration': 0.5, 'label': 'Drive Burwood', 'type': 'Travel'},
    {'day': 3, 'start': 9.75, 'duration': 3.25, 'label': 'Class: Pentateuch', 'type': 'Fixed'},
    {'day': 3, 'start': 13.0, 'duration': 1.5, 'label': 'Pastor Meetup', 'type': 'Personal'},
    {'day': 3, 'start': 14.5, 'duration': 0.5, 'label': 'Drive Home', 'type': 'Travel'},
    {'day': 3, 'start': 15.0, 'duration': 0.75, 'label': 'Transition Buffer', 'type': 'Personal'},
    {'day': 3, 'start': 15.75, 'duration': 2.0, 'label': 'Deep Work: Elaborative Int.', 'type': 'DeepWork'},
    {'day': 3, 'start': 17.75, 'duration': 1.0, 'label': 'Dinner', 'type': 'Personal'},
    {'day': 3, 'start': 18.75, 'duration': 2.0, 'label': 'Deep Work: Interleaved Syntax', 'type': 'DeepWork'},

    # FRIDAY (Day 4) - SABBATH 1
    {'day': 4, 'start': 8.0, 'duration': 0.5, 'label': 'Wake & Bible', 'type': 'Personal'},
    {'day': 4, 'start': 9.5, 'duration': 0.5, 'label': 'Drive WPH', 'type': 'Travel'},
    {'day': 4, 'start': 10.0, 'duration': 1.0, 'label': 'Client: WPH', 'type': 'Client'},
    {'day': 4, 'start': 11.0, 'duration': 0.5, 'label': 'Drive to Wife', 'type': 'Travel'},
    {'day': 4, 'start': 11.5, 'duration': 3.0, 'label': 'Sabbath Rest (Wife Time)', 'type': 'Sabbath'},
    {'day': 4, 'start': 14.5, 'duration': 0.5, 'label': 'Drive Home', 'type': 'Travel'},
    {'day': 4, 'start': 15.0, 'duration': 2.0, 'label': 'Deep Work: Blank Sheet', 'type': 'DeepWork'},
    {'day': 4, 'start': 17.0, 'duration': 1.5, 'label': 'Dinner', 'type': 'Personal'},
    {'day': 4, 'start': 18.5, 'duration': 2.0, 'label': 'Deep Work: Visual Mnemonic', 'type': 'DeepWork'},

    # SATURDAY (Day 5) - SABBATH 2
    {'day': 5, 'start': 8.0, 'duration': 4.0, 'label': 'Sabbath Rest', 'type': 'Sabbath'},
    {'day': 5, 'start': 12.0, 'duration': 1.0, 'label': 'Lunch', 'type': 'Personal'},
    {'day': 5, 'start': 13.0, 'duration': 2.0, 'label': 'Deep Work: Concept Mapping', 'type': 'DeepWork'},
    {'day': 5, 'start': 15.5, 'duration': 2.0, 'label': 'Deep Work: Cumulative Review', 'type': 'DeepWork'},
    {'day': 5, 'start': 17.5, 'duration': 1.5, 'label': 'Dinner', 'type': 'Personal'},

    # SUNDAY (Day 6)
    {'day': 6, 'start': 8.0, 'duration': 0.5, 'label': 'Wake & Bible', 'type': 'Personal'},
    {'day': 6, 'start': 8.5, 'duration': 0.5, 'label': 'Drive Church', 'type': 'Travel'},
    {'day': 6, 'start': 9.0, 'duration': 7.0, 'label': 'Church (Service/Serving)', 'type': 'Fixed'},
    {'day': 6, 'start': 16.0, 'duration': 0.5, 'label': 'Drive Home', 'type': 'Travel'},
    {'day': 6, 'start': 16.5, 'duration': 0.75, 'label': 'Transition Buffer', 'type': 'Personal'},
    {'day': 6, 'start': 17.25, 'duration': 1.5, 'label': 'Dinner', 'type': 'Personal'},
]

colors = {
    'Fixed': '#EF5350', 'Travel': '#90A4AE', 'Client': '#42A5F5',
    'DeepWork': '#66BB6A', 'Admin': '#AB47BC', 'Sabbath': '#FFA726', 'Personal': '#8D6E63'
}

# 3. RENDER LOGIC
def setup_visuals(ax, is_iphone=False):
    ax.set_ylim(23, 6) # 6 AM to 11 PM
    ax.grid(True, axis='y', color='#333333', linestyle='-', linewidth=0.5, alpha=0.5, zorder=0)
    
    # Time-Line (Left Column)
    hours = range(6, 24)
    ax.set_yticks(hours)
    ax.set_yticklabels([f"{h}" for h in hours], color='#AAAAAA', fontsize=11, fontweight='bold', va='center')
    ax.tick_params(axis='y', which='major', pad=8, length=0)
    
    ax.set_facecolor('#000000' if is_iphone else '#1E1E1E')
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(axis='x', length=0)

def render_device(fig, ax, data, filename, is_iphone=False, day_idx=None):
    setup_visuals(ax, is_iphone)
    
    # Highlight Today (PC/iPad only)
    if not is_iphone:
        # TIMEZONE FIX: Force Sydney Time (UTC+11)
        utc_now = datetime.datetime.now(datetime.timezone.utc)
        sydney_now = utc_now + datetime.timedelta(hours=11)
        today = sydney_now.weekday()
        ax.add_patch(patches.Rectangle((today-0.5, 6), 1, 18, color='#333333', alpha=0.3, zorder=0))

    for e in data:
        # PYTHON SAFETY FILTER: REMOVE BIRTHDAYS
        if 'birthday' in e['label'].lower(): continue

        if day_idx is not None and e['day'] != day_idx: continue
        x = 0 if day_idx is not None else e['day']
        
        # Draw Block
        width = 0.85 if is_iphone else 0.9
        rect = patches.FancyBboxPatch((x-(width/2), e['start']), width, e['duration'], 
                                      boxstyle="round,pad=0.02", facecolor=colors.get(e['type'], '#555'), zorder=2)
        ax.add_patch(rect)
        
        # Text
        label = textwrap.fill(e['label'], width=12 if is_iphone else 15)
        ax.text(x, e['start']+(e['duration']/2), label, ha='center', va='center', 
                color='white', fontweight='bold', fontsize=10 if is_iphone else 9, zorder=3)

    # LAYOUT ADJUSTMENTS
    if is_iphone:
        # Left: Room for numbers. Top: Room for Clock.
        plt.subplots_adjust(left=0.18, right=0.95, top=0.75, bottom=0.05)
        plt.savefig(os.path.join(save_folder, filename), dpi=300) 
    else:
        plt.savefig(os.path.join(save_folder, filename), dpi=200, bbox_inches='tight')
    
    print(f"Saved: {filename}")

# 4. EXECUTION
if __name__ == "__main__":
    # TIMEZONE FIX: Force Sydney Time (UTC+11)
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    sydney_now = utc_now + datetime.timedelta(hours=11)
    
    # iPhone Target: If after 8 PM, show tomorrow
    target = sydney_now + datetime.timedelta(days=1) if sydney_now.hour >= 20 else sydney_now

    # PC
    fig_pc, ax_pc = plt.subplots(figsize=(16, 9))
    fig_pc.patch.set_facecolor('#1E1E1E')
    ax_pc.set_xlim(-0.5, 6.5)
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ax_pc.xaxis.tick_top()
    ax_pc.set_xticks(range(7))
    ax_pc.set_xticklabels(days, fontsize=12, color='white')
    render_device(fig_pc, ax_pc, schedule_data, 'pc_wallpaper.png')

    # iPad
    fig_pad, ax_pad = plt.subplots(figsize=(12, 9))
    fig_pad.patch.set_facecolor('#1E1E1E')
    ax_pad.set_xlim(-0.5, 6.5)
    ax_pad.xaxis.tick_top()
    ax_pad.set_xticks(range(7))
    ax_pad.set_xticklabels(days, fontsize=11, color='white')
    render_device(fig_pad, ax_pad, schedule_data, 'ipad_wallpaper.png')

    # iPhone (Daily)
    fig_ph, ax_ph = plt.subplots(figsize=(9, 19.5)) 
    fig_ph.patch.set_facecolor('#000000') 
    ax_ph.set_xlim(-0.5, 0.5)
    ax_ph.set_xticklabels([]) 
    render_device(fig_ph, ax_ph, schedule_data, 'iphone_daily.png', True, target.weekday())
