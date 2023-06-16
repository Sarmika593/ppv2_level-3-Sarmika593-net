{"payload":{"allShortcutsEnabled":true,"fileTree":{"":{"items":[{"name":"age.py","path":"age.py","contentType":"file"},{"name":"caterpillar.py","path":"caterpillar.py","contentType":"file"},{"name":"kaleido_spiral.py","path":"kaleido_spiral.py","contentType":"file"},{"name":"robot_builder.py","path":"robot_builder.py","contentType":"file"},{"name":"screen_pet.py","path":"screen_pet.py","contentType":"file"}],"totalCount":5}},"fileTreeProcessingTime":1.730866,"foldersToFetch":[],"reducedMotionEnabled":"system","repo":{"id":626764713,"defaultBranch":"main","name":"PPV2_Level-3","ownerLogin":"YITExperiments","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-04-12T11:17:49.000+05:30","ownerAvatar":"https://avatars.githubusercontent.com/u/128239821?v=4","public":true,"private":false,"isOrgOwned":false},"refInfo":{"name":"main","listCacheKey":"v0:1681278518.0","canEdit":true,"refType":"branch","currentOid":"970aed74d73134ecd64ed6a205efb6893b2d0d2c"},"path":"screen_pet.py","currentUser":{"id":136614440,"login":"Sarmika593-net","userEmail":"nirojagananathan68@gmail.com"},"blob":{"rawBlob":"from tkinter import HIDDEN, NORMAL,Tk, Canvas\r\ndef toggle_eyes():\r\n    current_color = c.itemcget(eye_left, 'fill')\r\n    new_color = c.body_color if current_color == 'white' else 'white'\r\n    current_state = c.itemcget(pupil_left, 'state')\r\n    new_state = NORMAL if current_state == HIDDEN else HIDDEN\r\n    c.itemconfigure(pupil_left, state=new_state)\r\n    c.itemconfigure(pupil_right, state=new_state)\r\n    c.itemconfigure(eye_left, fill=new_color)\r\n    c.itemconfigure(eye_right, fill=new_color)\r\n\r\ndef blink():\r\n    toggle_eyes()\r\n    root.after(250, toggle_eyes)\r\n    root.after(3000, blink)\r\nroot=Tk()\r\n\r\nc=Canvas(root, width=400, height=400)\r\nc.configure(bg='dark blue',highlightthickness=0)\r\n\r\nc.body_color = 'SkyBlue1'\r\nbody = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)\r\near_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)\r\near_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, \\\r\n                             fill=c.body_color)\r\n\r\nfoot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill= c.body_color)\r\nfoot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill= c.body_color)\r\neye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')\r\npupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')\r\neye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')\r\npupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')\r\nmouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)\r\n\r\nmouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)\r\nmouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)\r\ncheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)\r\ncheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)\r\n\r\nc.pack()\r\n\r\nroot.after(1000, blink)\r\ndef show_happy(event):\r\n    if (20 <= event.x <= 350) and (20 <= event.y <= 350):\r\n        c.itemconfigure(cheek_left, state=NORMAL)\r\n        c.itemconfigure(cheek_right, state=NORMAL)\r\n        c.itemconfigure(mouth_happy, state=NORMAL)\r\n        c.itemconfigure(mouth_normal, state=HIDDEN)\r\n        c.itemconfigure(mouth_sad, state=HIDDEN)\r\n    return\r\ndef hide_happy(event):\r\n    c.itemconfigure(cheek_left, state=HIDDEN)\r\n    c.itemconfigure(cheek_right, state=HIDDEN)\r\n    c.itemconfigure(mouth_happy, state=HIDDEN)\r\n    c.itemconfigure(mouth_normal, state=NORMAL)\r\n    c.itemconfigure(mouth_sad, state=HIDDEN)\r\n    return\r\nc.bind('<Motion>', show_happy)\r\nc.bind('<Leave>', hide_happy)\r\nroot.mainloop()\r\n\r\n\r\n\r\n","colorizedLines":null,"stylingDirectives":[[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":12,"cssClass":"pl-s1"},{"start":13,"end":19,"cssClass":"pl-k"},{"start":20,"end":26,"cssClass":"pl-v"},{"start":28,"end":34,"cssClass":"pl-v"},{"start":35,"end":37,"cssClass":"pl-v"},{"start":39,"end":45,"cssClass":"pl-v"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":15,"cssClass":"pl-en"}],[{"start":4,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":21,"cssClass":"pl-s1"},{"start":22,"end":30,"cssClass":"pl-en"},{"start":31,"end":39,"cssClass":"pl-s1"},{"start":41,"end":47,"cssClass":"pl-s"}],[{"start":4,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":17,"cssClass":"pl-s1"},{"start":18,"end":28,"cssClass":"pl-s1"},{"start":29,"end":31,"cssClass":"pl-k"},{"start":32,"end":45,"cssClass":"pl-s1"},{"start":46,"end":48,"cssClass":"pl-c1"},{"start":49,"end":56,"cssClass":"pl-s"},{"start":57,"end":61,"cssClass":"pl-k"},{"start":62,"end":69,"cssClass":"pl-s"}],[{"start":4,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":21,"cssClass":"pl-s1"},{"start":22,"end":30,"cssClass":"pl-en"},{"start":31,"end":41,"cssClass":"pl-s1"},{"start":43,"end":50,"cssClass":"pl-s"}],[{"start":4,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":22,"cssClass":"pl-v"},{"start":23,"end":25,"cssClass":"pl-k"},{"start":26,"end":39,"cssClass":"pl-s1"},{"start":40,"end":42,"cssClass":"pl-c1"},{"start":43,"end":49,"cssClass":"pl-v"},{"start":50,"end":54,"cssClass":"pl-k"},{"start":55,"end":61,"cssClass":"pl-v"}],[{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":19,"cssClass":"pl-en"},{"start":20,"end":30,"cssClass":"pl-s1"},{"start":32,"end":37,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":38,"end":47,"cssClass":"pl-s1"}],[{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":19,"cssClass":"pl-en"},{"start":20,"end":31,"cssClass":"pl-s1"},{"start":33,"end":38,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-c1"},{"start":39,"end":48,"cssClass":"pl-s1"}],[{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":19,"cssClass":"pl-en"},{"start":20,"end":28,"cssClass":"pl-s1"},{"start":30,"end":34,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-c1"},{"start":35,"end":44,"cssClass":"pl-s1"}],[{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":19,"cssClass":"pl-en"},{"start":20,"end":29,"cssClass":"pl-s1"},{"start":31,"end":35,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-c1"},{"start":36,"end":45,"cssClass":"pl-s1"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":9,"cssClass":"pl-en"}],[{"start":4,"end":15,"cssClass":"pl-en"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":9,"end":14,"cssClass":"pl-en"},{"start":15,"end":18,"cssClass":"pl-c1"},{"start":20,"end":31,"cssClass":"pl-s1"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":9,"end":14,"cssClass":"pl-en"},{"start":15,"end":19,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-s1"}],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":4,"end":5,"cssClass":"pl-c1"},{"start":5,"end":7,"cssClass":"pl-v"}],[],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":1,"end":2,"cssClass":"pl-c1"},{"start":2,"end":8,"cssClass":"pl-v"},{"start":9,"end":13,"cssClass":"pl-s1"},{"start":15,"end":20,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":21,"end":24,"cssClass":"pl-c1"},{"start":26,"end":32,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":33,"end":36,"cssClass":"pl-c1"}],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":11,"cssClass":"pl-en"},{"start":12,"end":14,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":15,"end":26,"cssClass":"pl-s"},{"start":27,"end":45,"cssClass":"pl-s1"},{"start":45,"end":46,"cssClass":"pl-c1"},{"start":46,"end":47,"cssClass":"pl-c1"}],[],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":25,"cssClass":"pl-s"}],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":8,"cssClass":"pl-s1"},{"start":9,"end":20,"cssClass":"pl-en"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":25,"end":27,"cssClass":"pl-c1"},{"start":29,"end":32,"cssClass":"pl-c1"},{"start":34,"end":37,"cssClass":"pl-c1"},{"start":39,"end":46,"cssClass":"pl-s1"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":47,"end":48,"cssClass":"pl-s1"},{"start":49,"end":59,"cssClass":"pl-s1"},{"start":61,"end":65,"cssClass":"pl-s1"},{"start":65,"end":66,"cssClass":"pl-c1"},{"start":66,"end":67,"cssClass":"pl-s1"},{"start":68,"end":78,"cssClass":"pl-s1"}],[{"start":0,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":12,"cssClass":"pl-s1"},{"start":13,"end":27,"cssClass":"pl-en"},{"start":28,"end":30,"cssClass":"pl-c1"},{"start":32,"end":34,"cssClass":"pl-c1"},{"start":36,"end":38,"cssClass":"pl-c1"},{"start":40,"end":42,"cssClass":"pl-c1"},{"start":44,"end":47,"cssClass":"pl-c1"},{"start":49,"end":51,"cssClass":"pl-c1"},{"start":53,"end":60,"cssClass":"pl-s1"},{"start":60,"end":61,"cssClass":"pl-c1"},{"start":61,"end":62,"cssClass":"pl-s1"},{"start":63,"end":73,"cssClass":"pl-s1"},{"start":75,"end":79,"cssClass":"pl-s1"},{"start":79,"end":80,"cssClass":"pl-c1"},{"start":80,"end":81,"cssClass":"pl-s1"},{"start":82,"end":92,"cssClass":"pl-s1"}],[{"start":0,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":28,"cssClass":"pl-en"},{"start":29,"end":32,"cssClass":"pl-c1"},{"start":34,"end":36,"cssClass":"pl-c1"},{"start":38,"end":41,"cssClass":"pl-c1"},{"start":43,"end":45,"cssClass":"pl-c1"},{"start":47,"end":50,"cssClass":"pl-c1"},{"start":52,"end":54,"cssClass":"pl-c1"},{"start":56,"end":63,"cssClass":"pl-s1"},{"start":63,"end":64,"cssClass":"pl-c1"},{"start":64,"end":65,"cssClass":"pl-s1"},{"start":66,"end":76,"cssClass":"pl-s1"}],[{"start":29,"end":33,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-c1"},{"start":34,"end":35,"cssClass":"pl-s1"},{"start":36,"end":46,"cssClass":"pl-s1"}],[],[{"start":0,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":25,"cssClass":"pl-en"},{"start":26,"end":28,"cssClass":"pl-c1"},{"start":30,"end":33,"cssClass":"pl-c1"},{"start":35,"end":38,"cssClass":"pl-c1"},{"start":40,"end":43,"cssClass":"pl-c1"},{"start":45,"end":52,"cssClass":"pl-s1"},{"start":52,"end":53,"cssClass":"pl-c1"},{"start":53,"end":54,"cssClass":"pl-s1"},{"start":55,"end":65,"cssClass":"pl-s1"},{"start":67,"end":71,"cssClass":"pl-s1"},{"start":71,"end":72,"cssClass":"pl-c1"},{"start":73,"end":74,"cssClass":"pl-s1"},{"start":75,"end":85,"cssClass":"pl-s1"}],[{"start":0,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":14,"cssClass":"pl-s1"},{"start":15,"end":26,"cssClass":"pl-en"},{"start":27,"end":30,"cssClass":"pl-c1"},{"start":32,"end":35,"cssClass":"pl-c1"},{"start":37,"end":40,"cssClass":"pl-c1"},{"start":42,"end":45,"cssClass":"pl-c1"},{"start":47,"end":54,"cssClass":"pl-s1"},{"start":54,"end":55,"cssClass":"pl-c1"},{"start":55,"end":56,"cssClass":"pl-s1"},{"start":57,"end":67,"cssClass":"pl-s1"},{"start":69,"end":73,"cssClass":"pl-s1"},{"start":73,"end":74,"cssClass":"pl-c1"},{"start":75,"end":76,"cssClass":"pl-s1"},{"start":77,"end":87,"cssClass":"pl-s1"}],[{"start":0,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":12,"cssClass":"pl-s1"},{"start":13,"end":24,"cssClass":"pl-en"},{"start":25,"end":28,"cssClass":"pl-c1"},{"start":30,"end":33,"cssClass":"pl-c1"},{"start":35,"end":38,"cssClass":"pl-c1"},{"start":40,"end":43,"cssClass":"pl-c1"},{"start":45,"end":52,"cssClass":"pl-s1"},{"start":52,"end":53,"cssClass":"pl-c1"},{"start":53,"end":60,"cssClass":"pl-s"},{"start":62,"end":66,"cssClass":"pl-s1"},{"start":66,"end":67,"cssClass":"pl-c1"},{"start":67,"end":74,"cssClass":"pl-s"}],[{"start":0,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":14,"cssClass":"pl-s1"},{"start":15,"end":26,"cssClass":"pl-en"},{"start":27,"end":30,"cssClass":"pl-c1"},{"start":32,"end":35,"cssClass":"pl-c1"},{"start":37,"end":40,"cssClass":"pl-c1"},{"start":42,"end":45,"cssClass":"pl-c1"},{"start":47,"end":54,"cssClass":"pl-s1"},{"start":54,"end":55,"cssClass":"pl-c1"},{"start":55,"end":62,"cssClass":"pl-s"},{"start":64,"end":68,"cssClass":"pl-s1"},{"start":68,"end":69,"cssClass":"pl-c1"},{"start":69,"end":76,"cssClass":"pl-s"}],[{"start":0,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":25,"cssClass":"pl-en"},{"start":26,"end":29,"cssClass":"pl-c1"},{"start":31,"end":34,"cssClass":"pl-c1"},{"start":36,"end":39,"cssClass":"pl-c1"},{"start":41,"end":44,"cssClass":"pl-c1"},{"start":46,"end":53,"cssClass":"pl-s1"},{"start":53,"end":54,"cssClass":"pl-c1"},{"start":54,"end":61,"cssClass":"pl-s"},{"start":63,"end":67,"cssClass":"pl-s1"},{"start":67,"end":68,"cssClass":"pl-c1"},{"start":68,"end":75,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":15,"cssClass":"pl-s1"},{"start":16,"end":27,"cssClass":"pl-en"},{"start":28,"end":31,"cssClass":"pl-c1"},{"start":33,"end":36,"cssClass":"pl-c1"},{"start":38,"end":41,"cssClass":"pl-c1"},{"start":43,"end":46,"cssClass":"pl-c1"},{"start":48,"end":55,"cssClass":"pl-s1"},{"start":55,"end":56,"cssClass":"pl-c1"},{"start":56,"end":63,"cssClass":"pl-s"},{"start":65,"end":69,"cssClass":"pl-s1"},{"start":69,"end":70,"cssClass":"pl-c1"},{"start":70,"end":77,"cssClass":"pl-s"}],[{"start":0,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":16,"cssClass":"pl-s1"},{"start":17,"end":28,"cssClass":"pl-en"},{"start":29,"end":32,"cssClass":"pl-c1"},{"start":34,"end":37,"cssClass":"pl-c1"},{"start":39,"end":42,"cssClass":"pl-c1"},{"start":44,"end":47,"cssClass":"pl-c1"},{"start":49,"end":52,"cssClass":"pl-c1"},{"start":54,"end":57,"cssClass":"pl-c1"},{"start":59,"end":65,"cssClass":"pl-s1"},{"start":65,"end":66,"cssClass":"pl-c1"},{"start":66,"end":67,"cssClass":"pl-c1"},{"start":69,"end":74,"cssClass":"pl-s1"},{"start":74,"end":75,"cssClass":"pl-c1"},{"start":75,"end":76,"cssClass":"pl-c1"},{"start":78,"end":83,"cssClass":"pl-s1"},{"start":83,"end":84,"cssClass":"pl-c1"},{"start":84,"end":90,"cssClass":"pl-v"}],[],[{"start":0,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":15,"cssClass":"pl-s1"},{"start":16,"end":27,"cssClass":"pl-en"},{"start":28,"end":31,"cssClass":"pl-c1"},{"start":33,"end":36,"cssClass":"pl-c1"},{"start":38,"end":41,"cssClass":"pl-c1"},{"start":43,"end":46,"cssClass":"pl-c1"},{"start":48,"end":51,"cssClass":"pl-c1"},{"start":53,"end":56,"cssClass":"pl-c1"},{"start":58,"end":64,"cssClass":"pl-s1"},{"start":64,"end":65,"cssClass":"pl-c1"},{"start":65,"end":66,"cssClass":"pl-c1"},{"start":68,"end":73,"cssClass":"pl-s1"},{"start":73,"end":74,"cssClass":"pl-c1"},{"start":74,"end":75,"cssClass":"pl-c1"},{"start":77,"end":82,"cssClass":"pl-s1"},{"start":82,"end":83,"cssClass":"pl-c1"},{"start":83,"end":89,"cssClass":"pl-v"}],[{"start":0,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":25,"cssClass":"pl-en"},{"start":26,"end":29,"cssClass":"pl-c1"},{"start":31,"end":34,"cssClass":"pl-c1"},{"start":36,"end":39,"cssClass":"pl-c1"},{"start":41,"end":44,"cssClass":"pl-c1"},{"start":46,"end":49,"cssClass":"pl-c1"},{"start":51,"end":54,"cssClass":"pl-c1"},{"start":56,"end":62,"cssClass":"pl-s1"},{"start":62,"end":63,"cssClass":"pl-c1"},{"start":63,"end":64,"cssClass":"pl-c1"},{"start":66,"end":71,"cssClass":"pl-s1"},{"start":71,"end":72,"cssClass":"pl-c1"},{"start":72,"end":73,"cssClass":"pl-c1"},{"start":75,"end":80,"cssClass":"pl-s1"},{"start":80,"end":81,"cssClass":"pl-c1"},{"start":81,"end":87,"cssClass":"pl-v"}],[{"start":0,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":14,"cssClass":"pl-s1"},{"start":15,"end":26,"cssClass":"pl-en"},{"start":27,"end":29,"cssClass":"pl-c1"},{"start":31,"end":34,"cssClass":"pl-c1"},{"start":36,"end":39,"cssClass":"pl-c1"},{"start":41,"end":44,"cssClass":"pl-c1"},{"start":46,"end":53,"cssClass":"pl-s1"},{"start":53,"end":54,"cssClass":"pl-c1"},{"start":54,"end":60,"cssClass":"pl-s"},{"start":62,"end":66,"cssClass":"pl-s1"},{"start":66,"end":67,"cssClass":"pl-c1"},{"start":67,"end":73,"cssClass":"pl-s"},{"start":75,"end":80,"cssClass":"pl-s1"},{"start":80,"end":81,"cssClass":"pl-c1"},{"start":81,"end":87,"cssClass":"pl-v"}],[{"start":0,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":15,"cssClass":"pl-s1"},{"start":16,"end":27,"cssClass":"pl-en"},{"start":28,"end":31,"cssClass":"pl-c1"},{"start":33,"end":36,"cssClass":"pl-c1"},{"start":38,"end":41,"cssClass":"pl-c1"},{"start":43,"end":46,"cssClass":"pl-c1"},{"start":48,"end":55,"cssClass":"pl-s1"},{"start":55,"end":56,"cssClass":"pl-c1"},{"start":56,"end":62,"cssClass":"pl-s"},{"start":64,"end":68,"cssClass":"pl-s1"},{"start":68,"end":69,"cssClass":"pl-c1"},{"start":69,"end":75,"cssClass":"pl-s"},{"start":77,"end":82,"cssClass":"pl-s1"},{"start":82,"end":83,"cssClass":"pl-c1"},{"start":83,"end":89,"cssClass":"pl-v"}],[],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":6,"cssClass":"pl-en"}],[],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":10,"cssClass":"pl-en"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-s1"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":14,"cssClass":"pl-en"},{"start":15,"end":20,"cssClass":"pl-s1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":8,"end":10,"cssClass":"pl-c1"},{"start":11,"end":13,"cssClass":"pl-c1"},{"start":14,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-s1"},{"start":22,"end":24,"cssClass":"pl-c1"},{"start":25,"end":28,"cssClass":"pl-c1"},{"start":30,"end":33,"cssClass":"pl-c1"},{"start":35,"end":37,"cssClass":"pl-c1"},{"start":38,"end":40,"cssClass":"pl-c1"},{"start":41,"end":46,"cssClass":"pl-s1"},{"start":47,"end":48,"cssClass":"pl-s1"},{"start":49,"end":51,"cssClass":"pl-c1"},{"start":52,"end":55,"cssClass":"pl-c1"}],[{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":23,"cssClass":"pl-en"},{"start":24,"end":34,"cssClass":"pl-s1"},{"start":36,"end":41,"cssClass":"pl-s1"},{"start":41,"end":42,"cssClass":"pl-c1"},{"start":42,"end":48,"cssClass":"pl-v"}],[{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":23,"cssClass":"pl-en"},{"start":24,"end":35,"cssClass":"pl-s1"},{"start":37,"end":42,"cssClass":"pl-s1"},{"start":42,"end":43,"cssClass":"pl-c1"},{"start":43,"end":49,"cssClass":"pl-v"}],[{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":23,"cssClass":"pl-en"},{"start":24,"end":35,"cssClass":"pl-s1"},{"start":37,"end":42,"cssClass":"pl-s1"},{"start":42,"end":43,"cssClass":"pl-c1"},{"start":43,"end":49,"cssClass":"pl-v"}],[{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":23,"cssClass":"pl-en"},{"start":24,"end":36,"cssClass":"pl-s1"},{"start":38,"end":43,"cssClass":"pl-s1"},{"start":43,"end":44,"cssClass":"pl-c1"},{"start":44,"end":50,"cssClass":"pl-v"}],[{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":23,"cssClass":"pl-en"},{"start":24,"end":33,"cssClass":"pl-s1"},{"start":35,"end":40,"cssClass":"pl-s1"},{"start":40,"end":41,"cssClass":"pl-c1"},{"start":41,"end":47,"cssClass":"pl-v"}],[{"start":4,"end":10,"cssClass":"pl-k"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":14,"cssClass":"pl-en"},{"start":15,"end":20,"cssClass":"pl-s1"}],[{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":19,"cssClass":"pl-en"},{"start":20,"end":30,"cssClass":"pl-s1"},{"start":32,"end":37,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":38,"end":44,"cssClass":"pl-v"}],[{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":19,"cssClass":"pl-en"},{"start":20,"end":31,"cssClass":"pl-s1"},{"start":33,"end":38,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-c1"},{"start":39,"end":45,"cssClass":"pl-v"}],[{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":19,"cssClass":"pl-en"},{"start":20,"end":31,"cssClass":"pl-s1"},{"start":33,"end":38,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-c1"},{"start":39,"end":45,"cssClass":"pl-v"}],[{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":19,"cssClass":"pl-en"},{"start":20,"end":32,"cssClass":"pl-s1"},{"start":34,"end":39,"cssClass":"pl-s1"},{"start":39,"end":40,"cssClass":"pl-c1"},{"start":40,"end":46,"cssClass":"pl-v"}],[{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":19,"cssClass":"pl-en"},{"start":20,"end":29,"cssClass":"pl-s1"},{"start":31,"end":36,"cssClass":"pl-s1"},{"start":36,"end":37,"cssClass":"pl-c1"},{"start":37,"end":43,"cssClass":"pl-v"}],[{"start":4,"end":10,"cssClass":"pl-k"}],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":6,"cssClass":"pl-en"},{"start":7,"end":17,"cssClass":"pl-s"},{"start":19,"end":29,"cssClass":"pl-s1"}],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":6,"cssClass":"pl-en"},{"start":7,"end":16,"cssClass":"pl-s"},{"start":18,"end":28,"cssClass":"pl-s1"}],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":13,"cssClass":"pl-en"}],[],[],[]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/YITExperiments/PPV2_Level-3/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false,"repoAlertsPath":"/YITExperiments/PPV2_Level-3/security/dependabot","repoSecurityAndAnalysisPath":"/YITExperiments/PPV2_Level-3/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"screen_pet.py","displayUrl":"https://github.com/YITExperiments/PPV2_Level-3/blob/main/screen_pet.py?raw=true","headerInfo":{"blobSize":"2.68 KB","deleteInfo":{"deletePath":"https://github.com/YITExperiments/PPV2_Level-3/delete/main/screen_pet.py","deleteTooltip":"Fork this repository and delete the file"},"editInfo":{"editTooltip":"Fork this repository and edit the file"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"03eadd9","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FYITExperiments%2FPPV2_Level-3%2Fblob%2Fmain%2Fscreen_pet.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"63","truncatedSloc":"53"},"mode":"file"},"image":false,"isCodeownersFile":null,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","large":false,"loggedIn":true,"newDiscussionPath":"/YITExperiments/PPV2_Level-3/discussions/new","newIssuePath":"/YITExperiments/PPV2_Level-3/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/YITExperiments/PPV2_Level-3/blob/main/screen_pet.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/YITExperiments/PPV2_Level-3/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"YITExperiments","repoName":"PPV2_Level-3","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"toggle_eyes","kind":"function","identStart":51,"identEnd":62,"extentStart":47,"extentEnd":498,"fullyQualifiedName":"toggle_eyes","identUtf16":{"start":{"lineNumber":1,"utf16Col":4},"end":{"lineNumber":1,"utf16Col":15}},"extentUtf16":{"start":{"lineNumber":1,"utf16Col":0},"end":{"lineNumber":9,"utf16Col":46}}},{"name":"blink","kind":"function","identStart":506,"identEnd":511,"extentStart":502,"extentEnd":596,"fullyQualifiedName":"blink","identUtf16":{"start":{"lineNumber":11,"utf16Col":4},"end":{"lineNumber":11,"utf16Col":9}},"extentUtf16":{"start":{"lineNumber":11,"utf16Col":0},"end":{"lineNumber":14,"utf16Col":27}}},{"name":"root","kind":"constant","identStart":598,"identEnd":602,"extentStart":598,"extentEnd":607,"fullyQualifiedName":"root","identUtf16":{"start":{"lineNumber":15,"utf16Col":0},"end":{"lineNumber":15,"utf16Col":4}},"extentUtf16":{"start":{"lineNumber":15,"utf16Col":0},"end":{"lineNumber":15,"utf16Col":9}}},{"name":"c","kind":"constant","identStart":611,"identEnd":612,"extentStart":611,"extentEnd":648,"fullyQualifiedName":"c","identUtf16":{"start":{"lineNumber":17,"utf16Col":0},"end":{"lineNumber":17,"utf16Col":1}},"extentUtf16":{"start":{"lineNumber":17,"utf16Col":0},"end":{"lineNumber":17,"utf16Col":37}}},{"name":"body","kind":"constant","identStart":729,"identEnd":733,"extentStart":729,"extentEnd":808,"fullyQualifiedName":"body","identUtf16":{"start":{"lineNumber":21,"utf16Col":0},"end":{"lineNumber":21,"utf16Col":4}},"extentUtf16":{"start":{"lineNumber":21,"utf16Col":0},"end":{"lineNumber":21,"utf16Col":79}}},{"name":"ear_left","kind":"constant","identStart":810,"identEnd":818,"extentStart":810,"extentEnd":903,"fullyQualifiedName":"ear_left","identUtf16":{"start":{"lineNumber":22,"utf16Col":0},"end":{"lineNumber":22,"utf16Col":8}},"extentUtf16":{"start":{"lineNumber":22,"utf16Col":0},"end":{"lineNumber":22,"utf16Col":93}}},{"name":"ear_right","kind":"constant","identStart":905,"identEnd":914,"extentStart":905,"extentEnd":1033,"fullyQualifiedName":"ear_right","identUtf16":{"start":{"lineNumber":23,"utf16Col":0},"end":{"lineNumber":23,"utf16Col":9}},"extentUtf16":{"start":{"lineNumber":23,"utf16Col":0},"end":{"lineNumber":24,"utf16Col":47}}},{"name":"foot_left","kind":"constant","identStart":1037,"identEnd":1046,"extentStart":1037,"extentEnd":1123,"fullyQualifiedName":"foot_left","identUtf16":{"start":{"lineNumber":26,"utf16Col":0},"end":{"lineNumber":26,"utf16Col":9}},"extentUtf16":{"start":{"lineNumber":26,"utf16Col":0},"end":{"lineNumber":26,"utf16Col":86}}},{"name":"foot_right","kind":"constant","identStart":1125,"identEnd":1135,"extentStart":1125,"extentEnd":1213,"fullyQualifiedName":"foot_right","identUtf16":{"start":{"lineNumber":27,"utf16Col":0},"end":{"lineNumber":27,"utf16Col":10}},"extentUtf16":{"start":{"lineNumber":27,"utf16Col":0},"end":{"lineNumber":27,"utf16Col":88}}},{"name":"eye_left","kind":"constant","identStart":1215,"identEnd":1223,"extentStart":1215,"extentEnd":1290,"fullyQualifiedName":"eye_left","identUtf16":{"start":{"lineNumber":28,"utf16Col":0},"end":{"lineNumber":28,"utf16Col":8}},"extentUtf16":{"start":{"lineNumber":28,"utf16Col":0},"end":{"lineNumber":28,"utf16Col":75}}},{"name":"pupil_left","kind":"constant","identStart":1292,"identEnd":1302,"extentStart":1292,"extentEnd":1369,"fullyQualifiedName":"pupil_left","identUtf16":{"start":{"lineNumber":29,"utf16Col":0},"end":{"lineNumber":29,"utf16Col":10}},"extentUtf16":{"start":{"lineNumber":29,"utf16Col":0},"end":{"lineNumber":29,"utf16Col":77}}},{"name":"eye_right","kind":"constant","identStart":1371,"identEnd":1380,"extentStart":1371,"extentEnd":1447,"fullyQualifiedName":"eye_right","identUtf16":{"start":{"lineNumber":30,"utf16Col":0},"end":{"lineNumber":30,"utf16Col":9}},"extentUtf16":{"start":{"lineNumber":30,"utf16Col":0},"end":{"lineNumber":30,"utf16Col":76}}},{"name":"pupil_right","kind":"constant","identStart":1449,"identEnd":1460,"extentStart":1449,"extentEnd":1527,"fullyQualifiedName":"pupil_right","identUtf16":{"start":{"lineNumber":31,"utf16Col":0},"end":{"lineNumber":31,"utf16Col":11}},"extentUtf16":{"start":{"lineNumber":31,"utf16Col":0},"end":{"lineNumber":31,"utf16Col":78}}},{"name":"mouth_normal","kind":"constant","identStart":1529,"identEnd":1541,"extentStart":1529,"extentEnd":1620,"fullyQualifiedName":"mouth_normal","identUtf16":{"start":{"lineNumber":32,"utf16Col":0},"end":{"lineNumber":32,"utf16Col":12}},"extentUtf16":{"start":{"lineNumber":32,"utf16Col":0},"end":{"lineNumber":32,"utf16Col":91}}},{"name":"mouth_happy","kind":"constant","identStart":1624,"identEnd":1635,"extentStart":1624,"extentEnd":1714,"fullyQualifiedName":"mouth_happy","identUtf16":{"start":{"lineNumber":34,"utf16Col":0},"end":{"lineNumber":34,"utf16Col":11}},"extentUtf16":{"start":{"lineNumber":34,"utf16Col":0},"end":{"lineNumber":34,"utf16Col":90}}},{"name":"mouth_sad","kind":"constant","identStart":1716,"identEnd":1725,"extentStart":1716,"extentEnd":1804,"fullyQualifiedName":"mouth_sad","identUtf16":{"start":{"lineNumber":35,"utf16Col":0},"end":{"lineNumber":35,"utf16Col":9}},"extentUtf16":{"start":{"lineNumber":35,"utf16Col":0},"end":{"lineNumber":35,"utf16Col":88}}},{"name":"cheek_left","kind":"constant","identStart":1806,"identEnd":1816,"extentStart":1806,"extentEnd":1894,"fullyQualifiedName":"cheek_left","identUtf16":{"start":{"lineNumber":36,"utf16Col":0},"end":{"lineNumber":36,"utf16Col":10}},"extentUtf16":{"start":{"lineNumber":36,"utf16Col":0},"end":{"lineNumber":36,"utf16Col":88}}},{"name":"cheek_right","kind":"constant","identStart":1896,"identEnd":1907,"extentStart":1896,"extentEnd":1986,"fullyQualifiedName":"cheek_right","identUtf16":{"start":{"lineNumber":37,"utf16Col":0},"end":{"lineNumber":37,"utf16Col":11}},"extentUtf16":{"start":{"lineNumber":37,"utf16Col":0},"end":{"lineNumber":37,"utf16Col":90}}},{"name":"show_happy","kind":"function","identStart":2031,"identEnd":2041,"extentStart":2027,"extentEnd":2378,"fullyQualifiedName":"show_happy","identUtf16":{"start":{"lineNumber":42,"utf16Col":4},"end":{"lineNumber":42,"utf16Col":14}},"extentUtf16":{"start":{"lineNumber":42,"utf16Col":0},"end":{"lineNumber":49,"utf16Col":10}}},{"name":"hide_happy","kind":"function","identStart":2384,"identEnd":2394,"extentStart":2380,"extentEnd":2652,"fullyQualifiedName":"hide_happy","identUtf16":{"start":{"lineNumber":50,"utf16Col":4},"end":{"lineNumber":50,"utf16Col":14}},"extentUtf16":{"start":{"lineNumber":50,"utf16Col":0},"end":{"lineNumber":56,"utf16Col":10}}}]}},"csrf_tokens":{"/YITExperiments/PPV2_Level-3/branches":{"post":"y1zi_HmatZP5-lUpJjeVhvhj5126wSVieYAY5DXXH_W1AFzNPfZsxT5OHuAGDAnAKuobG57ZfPDx01p7FhGqTg"}}},"title":"PPV2_Level-3/screen_pet.py at main · YITExperiments/PPV2_Level-3","locale":"en"}