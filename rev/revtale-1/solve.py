from z3 import *

LEN = 33

flag = [BitVec(f'flag_{i}', 16) for i in range(LEN)]

s = Solver()

for b in flag[12:-5]:
	s.add(Or(
		And(b >= 0x30, b <= 0x39),
		And(b >= 0x41, b <= 0x5a),
		And(b >= 0x61, b <= 0x7a),
		b == ord('_'),
		b == ord('-'),
		#b == ord('{'),
		#b == ord('}'),
	))

s.add(flag[0] == ord('a'))
s.add(flag[1] == ord('m'))
s.add(flag[2] == ord('a'))
s.add(flag[3] == ord('t'))
s.add(flag[4] == ord('e'))
s.add(flag[5] == ord('u'))
s.add(flag[6] == ord('r'))
s.add(flag[7] == ord('s'))
s.add(flag[8] == ord('C'))
s.add(flag[9] == ord('T'))
s.add(flag[10] == ord('F'))
s.add(flag[11] == ord('{'))
s.add(flag[-1] == ord('}'))

#a = 'amateursCTF{'
a = flag

aa = (a[12] & 4095)
ab = (a[13] & 2047)
ac = (a[14] & 1023)
ad = (a[15] & 511)


s.add(a[12] == a[13])
s.add(a[12] != a[14])
s.add(ac == (aa - 2))

s.add(ab + 152 == 255)
s.add(ad + 133 == 255)

s.add(a[16] ^ 95 == 0)
s.add(a[17] ^ 119 == 0)
s.add(a[18] ^ 51 == 0)

s.add(a[19] == (2**6 | 31))

r = ["_", "l", "0", "v", "3", "%"]
s.add(a[19] == ord(r[0]))
s.add(a[20] == ord(r[1]))
s.add(a[21] == ord(r[2]))
s.add(a[22] == ord(r[3]))
s.add(a[23] == ord(r[4]))

s.add(a[24] == ord('_'))
s.add(a[25] == ord('v'))
s.add(a[26] == ord('m'))
s.add(a[27] == ord('_'))

s.add(a[28] == ord('b'))
s.add(a[29] == ord('3'))
s.add(a[30] == ord('3'))
s.add(a[31] == ord('f'))


if s.check() == sat:
	m = s.model()
	print(''.join([chr(m[b].as_long()) for b in flag]))

'''
funcs = [color_get_hue, color_get_green]
function scr_check_flag(argument0) //gml_Script_scr_check_flag
{
    l = string_lower(argument0)
    if ((string_pos("gaster", l) != 0))
    {
        window_set_caption("redacted")
        game_end(1)
    }
    if ((string_pos("frisk", l) != 0))
    {
        window_set_caption("don't make this hard")
        game_end(1)
    }
    if string_starts_with(argument0, "amateursCTF{")
    {
        if ((string_length(argument0) > 15))
        {
            a = scr_a(argument0)
            if ((a[12] == "{"))
            {
                window_set_caption("no")
                return 0;
            }
            for (i = 0; i < array_length(a); i++)
            {
            }
            aa = (ord(a[12]) & 4095)
            ab = (ord(a[13]) & 2047)
            ac = (ord(a[14]) & 1023)
            ad = (ord(a[15]) & 511)
            arr_op = array_reverse
            color_check = color_get_saturation
            if ((a[12] == a[13]) && (a[12] != a[14]))
            {
                if ((ac == (aa - 2)))
                {
                    if (((ab + 152) == self.color_check(16711935)) && ((ad + 133) == self.color_check(128)))
                    {
                        if (((obj_input_field.pk[0] ^ ord(a[16])) == 0))
                        {
                            if (((obj_input_field.pk[1] ^ ord(a[17])) == 0))
                            {
                                if (((obj_input_field.pk[2] ^ ord(a[18])) == 0))
                                {
                                    if ((ord(a[19]) == (power(2, 6) | 31)))
                                    {
                                        r = self.arr_op(["%", "3", "v", "0", "l", "_"], 0, 6)
                                        c = 0
                                        if ((a[19] == r[0]))
                                            c += 1
                                        if ((a[20] == r[1]))
                                            c += 2
                                        if ((a[21] == r[2]))
                                            c += 3
                                        if ((a[22] == r[3]))
                                            c += 4
                                        if ((a[23] == r[4]))
                                            c += 5
                                        if ((a[20] == a[21]))
                                            c += 5
                                        if ((c == 15))
                                        {
                                            if ((string_pos(file_text_read_string(file_text_open_read("f.txt")), argument0) != 0))
                                                return ((45887 == scr_c((((string_char_at(argument0, 29) + string_char_at(argument0, 30)) + string_char_at(argument0, 31)) + string_char_at(argument0, 32)))) && (ord(a[32]) == 125));
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            return 0;
        }
        else
            return 0;
    }
    else
        show_message(("flag wrapper missing... you entered " + argument0))
    return 0;
}
'''

