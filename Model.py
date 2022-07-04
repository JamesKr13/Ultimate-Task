from dataclasses import dataclass


@dataclass 
class subject:
    _abbreivation: str
    _subject_Name: str
    _teacher_code: str
    _teacher_name: list[str]
    _timetable: list[list[str]]
    _class_room: list[str]

    @property
    def abbreivation(self) -> str:
        return self._abbreivation
    
    @abbreivation.setter
    def abbreivation(self, new_name: str) -> None:
        if len(new_name) == len(self._abbreivation):
            self._abbreivation = new_name
        else:
            #warn
            pass
    
    @property
    def subject_Name(self) -> str:
        return self._subject_Name
    
    @subject_Name.setter
    def subject_Name(self, new_name: str) -> None:
       self._subject_Name = new_name

    @property
    def teacher_code(self) -> str:
        return self._teacher_code

    @teacher_code.setter
    def teacher_code(self, new_code: str) -> None:
        if len(new_code) == 3:
            self._teacher_code = new_code
        else:
            #warning
            pass
    
    @property
    def teacher_name(self) -> list[str]:
        return self._teacher_name
    
    @teacher_name.setter
    def teacher_name(self, new_teacher: str or list[str]) -> None:
        if type(new_teacher) is list:
            self._teacher_name = new_teacher
        
        elif type(new_teacher) is str:
            self._techer_name = new_teacher.split()
        
        else:
            #warning
            pass
    
    @property
    def timetable(self) -> list[list[str]]:
        return self._timetable
    
    @timetable.setter
    def timetable(self, new_times: list[list[str]]) -> None:
        self._timetable = new_times
    
    @property
    def class_room(self) -> list[str]:
        return self._class_room
    
    @class_room.setter
    def class_room(self, new_room: list[str]) -> None:
        self._class_room = new_room
    
@dataclass
class day_time:
    _days: str
    _spell_times: int
    _ako: bool
    _start_time: int
    _endtime: int


    @property
    def spell_times(self) -> list[int]:
        return self._spell_times
    
    @spell_times.setter
    def spell_times(self) -> None:
        pass

