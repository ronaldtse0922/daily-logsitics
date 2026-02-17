import matplotlib.pyplot as plt
import matplotlib.patches as patches
import textwrap, os, datetime

# CLOUD PATH: Save to current directory (.)
save_folder = "." 
schedule_data = [] # AI: PASTE YOUR LATEST SCHEDULE DATA HERE

colors = {'Fixed':'#EF5350','Travel':'#90A4AE','Client':'#42A5F5','DeepWork':'#66BB6A','Admin':'#AB47BC','Sabbath':'#FFA726','Personal':'#8D6E63'}

def render_all():
    for mode in ['pc', 'ipad', 'iphone']:
        if mode == 'pc': f, a, sz, dpi = plt.subplots(figsize=(16,9)), 'pc_wallpaper.png', 100
        elif mode == 'ipad': f, a, sz, dpi = plt.subplots(figsize=(12,9)), 'ipad_wallpaper.png', 100
        else: f, a, sz, dpi = plt.subplots(figsize=(9,19.5)), 'iphone_daily.png', 300
        
        a.set_ylim(23,6); a.set_facecolor('#1E1E1E' if mode != 'iphone' else '#000000')
        hours = range(6, 24)
        a.set_yticks(hours)
        a.set_yticklabels([f"{h}" for h in hours], color='#AAAAAA', fontsize=11, fontweight='bold')
        a.tick_params(axis='y', pad=8, length=0)
        a.grid(axis='y', color='#333', ls='--', alpha=0.5)
        for s in a.spines.values(): s.set_visible(False)

        if mode != 'iphone':
            days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
            a.set_xlim(-0.5, 6.5); a.xaxis.tick_top(); a.set_xticks(range(7)); a.set_xticklabels(days, color='white')
            today = datetime.datetime.now().weekday()
            a.add_patch(patches.Rectangle((today-0.5, 6), 1, 18, color='#333', alpha=0.3, zorder=0))
        else:
            a.set_xlim(-0.5, 0.5); a.set_xticks([])

        for e in schedule_data:
            if mode == 'iphone' and e['day'] != (datetime.datetime.now() + datetime.timedelta(days=1 if datetime.datetime.now().hour>=20 else 0)).weekday(): continue
            x = 0 if mode == 'iphone' else e['day']
            width = 0.85 if mode == 'iphone' else 0.9
            rect = patches.FancyBboxPatch((x-(width/2), e['start']), width, e['duration'], boxstyle="round,pad=0.02", facecolor=colors.get(e['type'], '#555'))
            a.add_patch(rect)
            a.text(x, e['start']+(e['duration']/2), textwrap.fill(e['label'],12), ha='center', va='center', color='white', weight='bold', size=10)
            
        if mode == 'iphone': plt.subplots_adjust(left=0.18, right=0.95, top=0.75, bottom=0.05)
        plt.savefig(os.path.join(save_folder, sz), dpi=dpi, bbox_inches='tight' if mode != 'iphone' else None)
        plt.close()

if __name__ == "__main__": render_all()
