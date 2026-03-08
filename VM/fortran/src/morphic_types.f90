module morphic_types
    implicit none
    private
    public :: verify_bilingual_integrity

contains

    subroutine verify_bilingual_integrity(task, hash_en, hash_jp)
        character(len=*), intent(in) :: task
        integer(kind=8), intent(in) :: hash_en, hash_jp
        
        character(len=10) :: status_bi
        
        ! 双方向一致確認
        if (hash_en == hash_jp .and. hash_en /= 0) then
            status_bi = "MATCH"
        else if (hash_en == 0) then
            status_bi = "FAIL(EN)"
        else
            status_bi = "MISMATCH"
        end if
        
        ! ログ出力
        print "(A, A, A, I0, A, I0, A, A)", &
            "TASK: ", task, " | EN: ", hash_en, " | JP: ", hash_jp, " | BILINGUAL: ", status_bi

    end subroutine verify_bilingual_integrity

end module morphic_types
