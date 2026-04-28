from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.utils import platform
import json
import os
import time
from datetime import datetime, timedelta
import plyer  # Untuk notifikasi & vibrator
from jnius import autoclass

class AlarmApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.alarms = self.load_alarms()
        self.active_alarm = None
        self.is_ringing = False
        
    def build(self):
        self.title = "🚨 AlarmKu"
        
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Header
        header = Label(
            text='🚨 ALARMKU',
            font_size='28sp',
            size_hint_y=None,
            height=60,
            color=(1, 0.2, 0.2, 1)
        )
        
        # Input waktu alarm
        input_layout = BoxLayout(size_hint_y=None, height=70, spacing=10)
        self.hour_input = TextInput(hint_text='Jam (1-23)', input_filter='int', multiline=False)
        self.min_input = TextInput(hint_text='Menit (0-59)', input_filter='int', multiline=False)
        add_btn = Button(text='➕ Tambah Alarm', background_color=(0.2, 0.8, 0.2, 1))
        add_btn.bind(on_press=self.add_alarm)
        
        input_layout.add_widget(self.hour_input)
        input_layout.add_widget(Label(text=':', size_hint_x=None, width=30))
        input_layout.add_widget(self.min_input)
        input_layout.add_widget(add_btn)
        
        # Daftar alarm
        scroll = ScrollView()
        self.alarms_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.alarms_layout.bind(minimum_height=self.alarms_layout.setter('height'))
        scroll.add_widget(self.alarms_layout)
        
        # Status waktu sekarang
        self.status_label = Label(text='', font_size='16sp', size_hint_y=None, height=40)
        
        # Tombol stop (hidden awal)
        self.stop_btn = Button(
            text='⏹️ STOP ALARM', 
            size_hint_y=None,
            height=0,
            background_color=(0.8, 0.2, 0.2, 1),
            font_size='20sp'
        )
        self.stop_btn.bind(on_press=self.stop_alarm)
        
        main_layout.add_widget(header)
        main_layout.add_widget(input_layout)
        main_layout.add_widget(self.status_label)
        main_layout.add_widget(scroll)
        main_layout.add_widget(self.stop_btn)
        
        # Start clock & alarm checker
        Clock.schedule_interval(self.update_clock, 1)
        Clock.schedule_interval(self.check_alarms, 30)  # Check tiap 30 detik
        
        self.refresh_alarms()
        return main_layout
    
    def add_alarm(self, instance):
        try:
            hour = int(self.hour_input.text)
            minute = int(self.min_input.text)
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                alarm_time = f"{hour:02d}:{minute:02d}"
                self.alarms.append({
                    'time': alarm_time,
                    'active': True,
                    'id': len(self.alarms) + 1
                })
                self.save_alarms()
                self.refresh_alarms()
                self.hour_input.text = ''
                self.min_input.text = ''
            else:
                self.show_popup("Error", "Jam 0-23, Menit 0-59!")
        except:
            self.show_popup("Error", "Masukkan angka yang valid!")
    
    def delete_alarm(self, instance):
        alarm_id = int(instance.text.split('ID:')[1].strip())
        self.alarms = [a for a in self.alarms if a['id'] != alarm_id]
        self.save_alarms()
        self.refresh_alarms()
    
    def toggle_alarm(self, instance):
        alarm_id = int(instance.text.split('ID:')[1].split(']')[0].strip())
        for alarm in self.alarms:
            if alarm['id'] == alarm_id:
                alarm['active'] = not alarm['active']
                break
        self.save_alarms()
        self.refresh_alarms()
    
    def refresh_alarms(self):
        self.alarms_layout.clear_widgets()
        for alarm in self.alarms:
            status = "✅" if alarm['active'] else "❌"
            btn_text = f"{status} {alarm['time']} [ID:{alarm['id']}]"
            
            btn = Button(
                text=btn_text,
                size_hint_y=None,
                height=60,
                background_color=(0.2, 0.6, 1, 1) if alarm['active'] else (0.6, 0.6, 0.6, 1)
            )
            btn.bind(on_press=self.toggle_alarm)
            delete_btn = Button(
                text='🗑️',
                size_hint_x=None,
                width=60,
                background_color=(0.8, 0.2, 0.2, 1)
            )
            delete_btn.bind(on_press=self.delete_alarm)
            
            row = BoxLayout(size_hint_y=None, height=60, spacing=10)
            row.add_widget(btn)
            row.add_widget(delete_btn)
            self.alarms_layout.add_widget(row)
    
    def update_clock(self, dt):
        now = datetime.now().strftime("%H:%M:%S")
        next_alarms = [a for a in self.alarms if a['active']]
        status = f"⏰ {now}"
        if next_alarms:
            status += f" | Alarms: {len(next_alarms)}"
        self.status_label.text = status
    
    def check_alarms(self, dt):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        
        for alarm in self.alarms:
            if alarm['active'] and alarm['time'] == current_time:
                self.ring_alarm(alarm)
                break
    
    def ring_alarm(self, alarm):
        if not self.is_ringing:
            self.is_ringing = True
            self.active_alarm = alarm
            
            # Show STOP button
            self.stop_btn.height = 70
            self.stop_btn.text = '🚨 ALARM BERBUNYI! STOP ALARM 🚨'
            
            # Notification
            try:
                plyer.notification.notify(
                    title='🚨 ALARM!',
                    message=f'Alarm {alarm["time"]} berbunyi!',
                    timeout=0
                )
            except:
                pass
            
            # Vibrate (Android)
            if platform == 'android':
                try:
                    PythonActivity = autoclass('org.kivy.android.PythonActivity')
                    Context = autoclass('android.content.Context')
                    Vibrator = autoclass('android.os.Vibrator')
                    
                    activity = PythonActivity.mActivity
                    vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)
                    
                    from android import api_version
                    if api_version >= 26:
                        VibrationEffect = autoclass('android.os.VibrationEffect')
                        vibrator.vibrate(VibrationEffect.createOneShot(1000, VibrationEffect.DEFAULT_AMPLITUDE))
                    else:
                        vibrator.vibrate(1000)
                except Exception as e:
                    print(f"Vibrate error: {e}")
    
    def stop_alarm(self, instance):
        self.is_ringing = False
        self.active_alarm = None
        self.stop_btn.height = 0
        
        # Snooze option
        popup = Popup(
            title='Alarm Dihentikan',
            content=Label(text='Mau snooze 5 menit?'),
            size_hint=(0.8, 0.4)
        )
        snooze_btn = Button(text='Snooze 5 Menit', size_hint_y=None, height=50)
        snooze_btn.bind(on_press=lambda x: self.snooze_alarm(popup))
        popup.content = BoxLayout(orientation='vertical')
        popup.content.add_widget(Label(text='Alarm dihentikan!'))
        popup.content.add_widget(snooze_btn)
        popup.open()
    
    def snooze_alarm(self, popup):
        if self.active_alarm:
            now = datetime.now()
            snooze_time = now + timedelta(minutes=5)
            hour, minute = snooze_time.hour, snooze_time.minute
            new_alarm = {
                'time': f"{hour:02d}:{minute:02d}",
                'active': True,
                'id': self.active_alarm['id']
            }
            self.alarms.append(new_alarm)
            self.save_alarms()
            self.refresh_alarms()
        popup.dismiss()
    
    def load_alarms(self):
        if os.path.exists('alarms.json'):
            try:
                with open('alarms.json', 'r') as f:
                    return json.load(f)
            except:
                pass
        return []
    
    def save_alarms(self):
        with open('alarms.json', 'w') as f:
            json.dump(self.alarms, f)

if __name__ == '__main__':
    AlarmApp().run()